from asyncio.subprocess import SubprocessStreamProtocol
from distutils.log import error
import json
import re

from flask import (
    Flask,
    abort,
    jsonify,
    request
)

from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from models import setup_db, Usuario

from functools import wraps
import uuid
import jwt
import datetime

#$env:FLASK_APP = "server"
#$env:FLASK_ENV = "development"
#flask run

def password_check(password):
    check = True
    if (len(password) <= 11):
        check = False
    elif not re.search("[a-z]", password):
        check = False
    elif not re.search("[A-Z]", password):
        check = False
    elif not re.search("[0-9]", password):
        check = False
    elif not re.search("[!#$%&?]", password):
        check = False
    elif re.search(r"\s", password):
        check = False
    return check

def create_app(test_config=None):
    app = Flask(__name__)
    database_name = 'almond_tec_test'
    database_path = 'postgresql://{}@{}/{}'.format('postgres:abc', 'localhost:5432', database_name)
    setup_db(app, database_path)

    #---------------CORS SETUP---------------

    CORS(app, origins=['http://192.168.1.4:8080/'])

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
        return response
    
    #---------------AUTENTICACIÓN GENERAL---------------

    def token_required(f):
        @wraps(f)
        def decorator(*args, **kwargs):
            token = None
            if 'Authorization' in request.headers:
                token = request.headers['Authorization']
        
            if not token:
                return jsonify({
                    'success': False,
                    'message':'Falta un token valido.'
                    })
            try:
                body = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                current_user = Usuario.query.filter_by(public_id=body['public_id']).first()
            except:
                return jsonify({
                    'success': False,
                    'message': 'Token invalido.'
                    })
        
            return f(current_user, *args, **kwargs)
        return decorator

    #---------------ENDPOINTS---------------

    @app.route('/login', methods=['POST'])
    def login():
        error_422 = False
        error_401 = True
        body = request.get_json()
        email = body.get('email', None)
        password = body.get('password', None)   
        
        if email is None or password is None: #incompleto
            error_422 = True
            abort(422)
        try:
            #------------AUTENTICACIÓN------------
            user_existe = Usuario.query.filter_by(email=email).first() #revisa si existe el user en la base de datos
            
            if not user_existe or not check_password_hash(user_existe.password, password):
                return jsonify({
                    'success': False,
                    'message' : 'Datos incorrectos.'
                })
            
            if user_existe and check_password_hash(user_existe.password, password):
                error_401 = False
                token = jwt.encode({'public_id' : user_existe.public_id, 
                                    'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=45)},
                                    app.config['SECRET_KEY'], "HS256")
                return jsonify({
                    'success': True,
                    'token' : token
                })
        
        except Exception as e:
            if error_422:
                abort(422)
            if error_401:
                abort(401)
            print(e)
            abort(500)

    @app.route('/signup', methods=['POST'])
    def signup():
        error_422 = False
        body = request.get_json()
        id = body.get('id', None)
        nombres = body.get('nombres', None)
        apellidos = body.get('apellidos', None)
        email = body.get('email', None)
        password = body.get('password', None)

        if (id is None
            or nombres is None
            or apellidos is None
            or email is None
            or password is None): #incompleto
            error_422 = True
            abort(422)

        try:
            #------------AUTENTICACIÓN------------
            code_existe = Usuario.query.filter_by(id=id).first() #si regresa un código -> existe en la base de datos
            email_existe = Usuario.query.filter_by(email=email).first() #si regresa un email -> existe en la base de datos

            flag = False
            if len(str(id)) != 9:
                flag = True
                mensaje = 'Código debe tener 9 caracteres.'
            if email[-12:]!="@utec.edu.pe":
                flag = True
                mensaje = 'Correo debe tener el formato @utec.edu.pe'
            if code_existe:
                flag = True
                mensaje = 'Código ya registrado.'
            if email_existe:
                flag = True
                mensaje = 'Correo ya registrado.'
            if not password_check(password):
                flag = True
                mensaje = 'Contraseña debe tener mínimo de 11 caracteres y al menos una mayúscula, una minúscula, un número y un caracter especial (!#$%&?)' 
            
            
            if flag:
                return jsonify({
                    'success': False,
                    'message': mensaje
                })

            new_user = Usuario(id=id, public_id=str(uuid.uuid4()), nombres=nombres, apellidos=apellidos, rol='E', email=email,
                        password=generate_password_hash(password, method='sha256'))
            new_id = new_user.insert()

            return jsonify({
                'success': True,
                'created': new_id
            })
                    
        except Exception as e:
            if error_422:
                abort(422)
            print(e)
            abort(500)
    
    @app.route('/user', methods=['GET'])
    @token_required
    def user(current_user):
        try:
            return jsonify(current_user.format())
        except Exception as e:
            print(e)
            abort(500)
    
    #---------------ERROR HANDLING---------------
   
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'code': 404,
            'message': 'not found'
        }), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            'success': False,
            'code': 401,
            'message': 'login required'
        }), 401

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 500,
            'message': 'internal server error'
        }), 500


    @app.errorhandler(405)
    def server_error(error):
        return jsonify({
            'success': False,
            'code': 405,
            'message': 'method not allowed'
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'code': 422,
            'message': 'unprocessable'
        }), 422

    return app
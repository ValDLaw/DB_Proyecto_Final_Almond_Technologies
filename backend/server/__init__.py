from ast import expr_context
from asyncio.subprocess import SubprocessStreamProtocol
from distutils.log import error
import json
from lib2to3.pgen2 import token
import re

from flask import (
    Flask,
    abort,
    flash,
    jsonify,
    request
)
from py import code
from sqlalchemy import null

from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from models import setup_db, Usuario, Estudiante, Profesor, ProfesorEstudiante, Curso, EstudianteCurso, Extra

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
    database_name = 'almond_tec'
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
            
            if not user_existe:
                return jsonify({
                    'success': False,
                    'message' : 'Correo no registrado.'
                })
            if not check_password_hash(user_existe.password, password):
                return jsonify({
                    'success': False,
                    'message' : 'Contraseña incorrecta.'
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
            elif email[-12:]!="@utec.edu.pe":
                flag = True
                mensaje = 'Correo debe tener el formato @utec.edu.pe'
            elif code_existe:
                flag = True
                mensaje = 'Código ya registrado.'
            elif email_existe:
                flag = True
                mensaje = 'Correo ya registrado.'
            elif not password_check(password):
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
                'message': 'Cuenta creada. Iniciar sesión.',
                'created': new_id
            })
                    
        except Exception as e:
            if error_422:
                abort(422)
            print(e)
            abort(500)

    @app.route('/password', methods=['PATCH'])
    def password():
        error_422 = False
        body = request.get_json()
        id = body.get('id', None)
        email = body.get('email', None)
        new_password = body.get('new_password', None)
        
        if (id is None
            or email is None
            or new_password is None): #incompleto
            error_422 = True
            abort(422)
        try:
            flag = False
            code_existe = Usuario.query.filter_by(id=id).first() #si regresa un código -> existe en la base de datos
            email_existe = Usuario.query.filter_by(email=email).first() #si regresa un email -> existe en la base de datos

            if not code_existe:
                flag = True
                mensaje = 'Código no registrado.'
            elif not email_existe:
                flag = True
                mensaje = 'Correo no registrado.'
            elif code_existe != email_existe:
                flag = True
                mensaje = 'El código y el correo no coinciden.'
            elif check_password_hash(code_existe.password, new_password):
                flag = True
                mensaje = 'Ingrese una nueva contraseña.'
            elif (not password_check(new_password)):
                flag = True
                mensaje = 'Contraseña debe tener mínimo de 11 caracteres y al menos una mayúscula, una minúscula, un número y un caracter especial (!#$%&?)' 

            if flag:
                return jsonify({
                    'success': False,
                    'message': mensaje
                })
            
            email_existe.password = generate_password_hash(new_password)
            code_existe.update()
                
            return jsonify({
                'success': True,
                'message': 'Contraseña cambiada.',
                'updated_id': id,
            })

        except Exception as e:
            if error_422:
                abort(422)
            print(e)
            abort(500)

    #valeria.espinoza@utec.edu.pe
    @app.route('/user', methods=['GET'])
    @token_required
    def user(current_user):
        try:
            if current_user.rol == 'E':
                estudiante = Estudiante.query.filter(Estudiante.id == current_user.id).one_or_none()
                return jsonify(estudiante.format())
            else:
                profesor = Profesor.query.filter(Profesor.id == current_user.id).one_or_none()
                return jsonify(profesor.format())
        except Exception as e:
            #print(e)
            abort(500)


    @app.route("/cursos/<curso_id>", methods=["GET"])
    def get_curso(curso_id):
        curso = Curso.query.filter(Curso.id == curso_id).one_or_none()
        if curso is None:
            abort(404, description="No se ha encontrado el curso.")
        return jsonify({
            "success" : True,
            "curso" : curso_id,
            "curso" : curso.format()
        })

    @app.route("/matricular/<curso_id>", methods = ["POST"])
    @token_required
    def create_curso(current_user, curso_id):
        error_404 = False
        try:
            curso = Curso.query.filter(Curso.id == curso_id).one_or_none()
            if curso is None:
                error_404 = True
                abort(404)
            
            curso_matriculado = EstudianteCurso(curso_id = curso_id, estudiante_id = current_user.id)
            curso_id = curso_matriculado.insert()

            return jsonify({
            "success" : True,
            "curso_matriculado_id" : curso_id,
            "curso_matriculado" : curso
        })

        except Exception as e:
            if error_404:
                abort(404)
            print(e)
            abort(500)
    
    @app.route("/abandonar/<curso_id>", methods = ["DELETE"])
    @token_required
    def delete_curso(current_user, curso_id):
        error_404 = False
        try:
            curso = Curso.query.filter(Curso.id == curso_id).one_or_none()
            if curso is None:
                error_404 = True
                abort(404)
            
            curso_abandonado = EstudianteCurso.query.filter(Curso.id == curso_id).one_or_none()
            curso_abandonado.delete()

            return jsonify({
            "success" : True,
            "curso_abandonado_id" : curso_id,
            "curso_abandonado" : curso
        })

        except Exception as e:
            if error_404:
                abort(404)
            print(e)
            abort(500)

    #---------- EXTRAS ---------
    @app.route("/extras", methods=["GET"])
    def get_extras():
        extras = Extra.query.all()
        return jsonify({
            "success" : True,
            "extras" : [extra.JSONSerialize() for extra in extras],
            "total_extras" : len(extras)
        })

    @app.route("/extras/<extra_nombre>", methods=["GET"])
    def get_extra(extra_nombre):
        extra = Extra.query.filter(Extra.nombre == extra_nombre).one_or_none()
        if extra is None:
            abort(404, description="No se ha encontrado el extra.")
        return jsonify({
            "success" : True,
            "extra" : extra.format()
        })

    @app.route("/cursos/<curso_id>/extras", methods=["POST"])
    def create_extra(curso_id):
        curso = Curso.query.filter(Curso.id == curso_id).one_or_none()

        if curso is None:
            abort(404, description = "No se ha encontrado el curso.")

        body = request.get_json()
        nombre = body.get("nombre", None)
        tema = body.get("tema", None)
        curso_id = body.get("curso_id", None)
        link = body.get("link", None)
        
        extra = Extra(nombre = nombre, tema = tema, curso_id = curso_id, link = link)
        extra_nombre = extra.insert()

        return jsonify({
            "success" : True,
            "extra_nombre" : extra_nombre
        })

    @app.route("/extras/<extra_nombre>", methods = ["PATCH"])
    def update_extra(extra_nombre):
        extra = Extra.query.filter(Extra.nombre == extra_nombre).one_or_none()

        if extra is None:
            abort(404)

        body = request.get_json()

        if "link" in body:
            extra.link = body.get("link")
        
        extra.update()

        return jsonify({
            "success" : True,
            "extra_nombre" : extra_nombre
        })

    @app.route("/extras/<extra_nombre>", methods = ["DELETE"])
    def delete_extra(extra_nombre):
        extra = Extra.query.filter(Extra.nombre == extra_nombre).one_or_none()

        if extra is None:
            abort(404, description = "No se ha encontrado el extra.")

        extra.delete()

        return jsonify({
            "success" : True,
            "extra_nombre" : extra_nombre
        })
    
    @app.route ('/logout', methods=['POST'])
    @token_required
    def logout(current_user):
        try:
            current_user.token = None
        except Exception as e:
            print(e)
            abort(500)
    
    '''
    @app.route("/comments/<estudiante_id>", methods = ["PATCH"])
    @token_required
    def update_student(current_user, estudiante_id):
        error_404 = False

        try:
            estudiante = Estudiante.query.filter(Estudiante.id == estudiante_id).one_or_none()
            if estudiante is None:
                error_404 = True
                abort(404)

            body = request.get_json()
            if 'cursos' in body:
                estudiante.cursos = body.get('cursos')

            cursos_estudiante = EstudianteCurso.query.filter_by(estudiante_id = current_user.id)
            cursos_inscritos_id =  []
            for curso in cursos_estudiante: cursos_inscritos_id.append(curso.curso_id)
            cursos_totales = Curso.query.all()
            cursos_inscritos =  []
            for curso in cursos_totales:
                if curso.id in cursos_inscritos_id: cursos_inscritos.append(curso)

        except:
            if error_404:
                abort(404)
            else:
                abort(500)
        
        lists = {list.id: {'id': list.id, 'name': list.name} for list in TodoLists.query.order_by('id').all()}
            if len(lists) == 0:
                abort(404)'''


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
    
from http import client
import unittest
import uuid

from flask_login import current_user
from requests import head
from server import create_app
from models import setup_db, Usuario
import json
from werkzeug.security import generate_password_hash, check_password_hash

#python -m unittest

class TestsAlmondTecApi(unittest.TestCase):
    def setUp(self):
        self.app = create_app() #de server
        self.client = self.app.test_client
        self.database_name = 'almond_tec_test' #nueva bdd
        self.database_path = 'postgresql://{}@{}/{}'.format('postgres:abc', 'localhost:5432', self.database_name)

        setup_db(self.app, self.database_path) #de models.py

        if not Usuario.query.filter_by(id=202110567).first():
            self.permanent_user = Usuario(id=202110567, public_id=str(uuid.uuid4()), nombres='Sofía', apellidos='García', rol='E', email='sofia.garcia@utec.edu.pe',
                            password=generate_password_hash('$ClaveSegura123', method='sha256'))
            self.permanent_user.insert()
            self.permanent_estudiante = Usuario(id=202110109, public_id=str(uuid.uuid4()), nombres='Valeria', apellidos='Espinoza', rol='E', email='valeria.espinoza@utec.edu.pe',
                            password=generate_password_hash('$ClaveSegura567', method='sha256'))
            self.permanent_estudiante.insert()
            self.permanent_profesor = Usuario(id=202110567, public_id=str(uuid.uuid4()), nombres='Marvin', apellidos='Abisrror', rol='P', email='m.abisrror@utec.edu.pe',
                            password=generate_password_hash('$ClaveSegura890', method='sha256'))
            self.permanent_profesor.insert()

        self.good_user = {
            'id': 202110123,
            'nombres': 'Sofía',
            'apellidos': 'Quintana',
            'email': 'sofia.quintana@utec.edu.pe',
            'password': '$ClaveSegura123'
            }
        
        self.bad_code = {
            'id': 2020,
            'nombres': 'Luisa',
            'apellidos': 'Mora',
            'email': 'luisa.mora@utec.edu.pe',
            'password': '$ClaveSegura123'
        }

        self.bad_email = {
            'id': 202110560,
            'nombres': 'Luisa',
            'apellidos': 'Mora',
            'email': 'luisa.mora@gmail.com',
            'password': '$ClaveSegura123'
        }
        
        self.repeated_code = {
            'id': 202110567,
            'nombres': 'Luisa',
            'apellidos': 'Mora',
            'email': 'luisa.mora@utec.edu.pe',
            'password': '$ClaveSegura123'
        }

        self.repeated_email = {
            'id': 202110560,
            'nombres': 'Luisa',
            'apellidos': 'Mora',
            'email': 'sofia.garcia@utec.edu.pe',
            'password': '$ClaveSegura123'
        }
        
        self.bad_password = {
            'id': 202110560,
            'nombres': 'Luisa',
            'apellidos': 'Mora',
            'email': 'luisa.mora@utec.edu.pe',
            'password': '123'
        }
        
        self.incomplete_user = {
            'id': 202110567,
            'nombres': 'Sofía',
            'apellidos': 'García',
            'email': 'sofia.garcia@utec.edu.pe'
        }

        self.user_login = {
            'email': 'sofia.garcia@utec.edu.pe',
            'password': '$ClaveSegura123'
        }

        self.estudiante_login = {
            'email': 'valeria.espinoza@utec.edu.pe',
            'password': '$ClaveSegura567'
        }

        self.profesor_login = {
            'email': 'm.abisrror@utec.edu.pe',
            'password': '$ClaveSegura890'
        }

        self.user_login_badkey = {
            'email': 'sofia.garcia@utec.edu.pe',
            'password': 'abc'
        }

        self.user_login_bademail = {
            'email': 'sofia.garcia@gmail.com',
            'password': '$ClaveSegura123'
        }

        self.new_curso = {
            'id': 124,
            'nombre': 'Desarrollo Basado en Plataformas',
            'profesor_id': 123456
            }
        
        self.new_extra = {
            'nombre': 'Kahoot',
            'tema': 'FLASK',
            'curso_id': 'Desarrollo Basado en Plataformas',
            'link': 'https://quizizz.com/join/quiz/6005c1ba7bff8b001d55cbeb/start?studentShare=true'
            }
            
    def test_user_not_autheticated(self):
        res = self.client().get('/user')
        data = json.loads(res.data)
        #print(data)

        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    def test_user_wrong_token(self):
        res = self.client().get('/user', headers={'Content-Type': 'application/json', 'Authorization': 'abc123'})
        data = json.loads(res.data)
        #print(data)

        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_user_authenticated(self):
        res0 = self.client().post('/login', json=self.user_login)
        data0 = json.loads(res0.data)
        token = data0['token']
        res = self.client().get('/user', headers={'Content-Type': 'application/json', 'Authorization': token})
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_login(self):
        res = self.client().post('/login', json=self.user_login)
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['token'])
    
    def test_login_wrongpassword(self):
        res = self.client().post('/login', json=self.user_login_badkey)
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    def test_login_wrongemail(self):
        res = self.client().post('/login', json=self.user_login_bademail)
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    def test_login_422(self):
        res = self.client().post('/login', json={})
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    #---------------Usuario: SIGNUP---------------
    def test_create_user(self):
        #como no se utiliza el método delete, lo hacemos manualmente
        u = Usuario.query.filter_by(id=202110123).first()
        if u: u.delete()
        
        res = self.client().post('/signup', json=self.good_user)
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
    
    def test_create_usermistake1(self):
        res = self.client().post('/signup', json=self.bad_code)
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    def test_create_usermistake2(self):
        res = self.client().post('/signup', json=self.bad_email)
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    def test_create_usermistake3(self):
        res = self.client().post('/signup', json=self.repeated_code)
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    def test_create_usermistake4(self):
        res = self.client().post('/signup', json=self.repeated_email)
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])
    
    def test_create_usermistake5(self):
        res = self.client().post('/signup', json=self.bad_password)
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_create_user_failed(self):
        res = self.client().post('/signup', json=self.incomplete_user)
        data = json.loads(res.data)
        #print(data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertTrue(data['message'])

    def test_user_estudiante(self):
        res0 = self.client().post('/login', json=self.user_login)
        data0 = json.loads(res0.data)
        token = data0['token']
        res = self.client().get('/user', headers={'Content-Type': 'application/json', 'Authorization': token})
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_user_profesor(self):
        res0 = self.client().post('/login', json=self.user_login)
        data0 = json.loads(res0.data)
        token = data0['token']
        print(token)
        res = self.client().get('/user', headers={'Content-Type': 'application/json', 'Authorization': token})
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def tearDown(self):
        del self.good_user
        del self.bad_code
        del self.bad_email
        del self.repeated_code
        del self.repeated_email
        del self.bad_password
        del self.incomplete_user
        del self.user_login
        del self.user_login_badkey
        del self.user_login_bademail
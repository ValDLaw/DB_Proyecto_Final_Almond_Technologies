    
from http import client
import unittest
import uuid

from flask_login import current_user
from requests import head
#from backend.models import Curso, Extra
from server import create_app
from models import setup_db, Usuario, Estudiante, Profesor, Curso, Extra
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
        
        if not Usuario.query.filter_by(id=202110123).first():
            self.permanent_user1.insert()
            self.permanent_estudiante = Estudiante(id=202110123, nombres='Sofía', apellidos='García')
            self.permanent_estudiante.insert()

        if not Usuario.query.filter_by(id=202110109).first():    
            self.permanent_user2 = Usuario(id=202110109, public_id=str(uuid.uuid4()), nombres='Valeria', apellidos='Espinoza', rol='E', email='valeria.espinoza@utec.edu.pe',
                                password=generate_password_hash('$ClaveSegura567', method='sha256'))
            self.permanent_user2.insert()

            self.permanent_estudiante = Estudiante(id=202110109, nombres='Valeria', apellidos='Espinoza')
            self.permanent_estudiante.insert()

        if not Usuario.query.filter_by(id=202120567).first():
            self.permanent_user3 = Usuario(id=202120567, public_id=str(uuid.uuid4()), nombres='Marvin', apellidos='Abisrror', rol='P', email='m.abisrror@utec.edu.pe',
                                password=generate_password_hash('$ClaveSegura890', method='sha256'))
            self.permanent_user3.insert()
            self.permanent_profesor = Profesor(id=202120567, nombres='Marvin', apellidos='Abisrror')
            self.permanent_profesor.insert()
        
        self.permanent_curso = Curso(id=124, nombre='Desarrollo Basado en Plataformas', profesor_id=202120567)
        if not Curso.query.filter_by(id=124).first():
            self.permanent_curso.insert()

        self.permanent_extra = Extra(nombre='Kahoot_FLASK', tema='FLASK', curso_id=124, link='https://www.youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A')
        if not Extra.query.filter_by(nombre='Kahoot_FLASK').first():
            self.permanent_extra.insert()

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
            'id': 202110109,
            'nombres': 'Luisa',
            'apellidos': 'Mora',
            'email': 'luisa.mora@utec.edu.pe',
            'password': '$ClaveSegura123'
        }

        self.repeated_email = {
            'id': 202110123,
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
            'nombre': 'Extra test',
            'tema': 'BLACKPINK',
            'curso_id': self.permanent_curso.id,
            'link': 'https://www.youtube.com/channel/UCOmHUn--16B90oW2L6FRR3A'
            }

        self.new_password_user = {
            'id': 202210567,
            'nombres': 'María',
            'apellidos': 'Perez',
            'email': 'maria.perez@utec.edu.pe',
            'password': '$ClaveSegura123'
        }

        self.new_password = {
            'id': 202110123,
            'email': 'sofia.garcia@utec.edu.pe',
            'new_password': '$ClaveSegura123' #cambiar clave antes de hacerlo
        }
            
    def test_change_password(self):
        res = self.client().patch('/password', json=self.new_password)
        data = json.loads(res.data)
        #print(data)

        self.assertEqual(data['success'], True)
        self.assertTrue(data['updated_id'])
        self.assertTrue(data['message'])


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

    def test_estudiante_authenticated(self):
        res0 = self.client().post('/login', json=self.estudiante_login)
        data0 = json.loads(res0.data)
        token = data0['token']
        res = self.client().get('/user', headers={'Content-Type': 'application/json', 'Authorization': token})
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['nombres'])
        self.assertTrue(data['apellidos'])
        self.assertEqual(data['rol'], 'estudiante')

    def test_profesor_authenticated(self):
        res0 = self.client().post('/login', json=self.profesor_login)
        data0 = json.loads(res0.data)
        token = data0['token']
        res = self.client().get('/user', headers={'Content-Type': 'application/json', 'Authorization': token})
        data = json.loads(res.data)
        #print(data)
        
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['nombres'])
        self.assertTrue(data['apellidos'])
        self.assertEqual(data['rol'], 'profesor')

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


    def tearDown(self):
        for user in Usuario.query.all():
            user.delete()
        for estudiante in Estudiante.query.all():
            estudiante.delete()
        for profesor in Profesor.query.all():
            profesor.delete()
        for curso in Curso.query.all():
            curso.delete()
        for extra in Extra.query.all():
            extra.delete()
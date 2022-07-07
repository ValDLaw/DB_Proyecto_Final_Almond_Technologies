from flask import jsonify
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup_db(app, database_path):
    app.secret_key = "proyecto_dbp"
    app.config['SQLALCHEMY_DATABASE_URI'] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)
    db.create_all()

class Usuario(UserMixin, db.Model): #antes UserMixin por Flask-Login
    __tablename__ = 'users'
    id = db.Column(db.BIGINT(), primary_key=True)
    nombres = db.Column(db.String(), nullable=False)
    apellidos = db.Column(db.String(), nullable=False)
    rol = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __init__ (self, id, nombres, apellidos, rol, email, password):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos
        self.rol = rol
        self.email = email
        self.password = password

    def format(self):
        return {
            'id': self.id,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'rol': self.rol,
            'email': self.email,
            'password': self.password
        }

    def __repr__(self):
        return 'Todo: id={}, nombres={}, apellidos={}, rol={}, email={}, password={}'.format(
            self.id, self.nombres, self.apellidos, self.rol, self.email, self.password)

    #def checkpassword(password):
    
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
        finally:
            db.session.close()

#----------Alumnos-------------

'''
class Estudiante(db.Model):
    __tablename__ = 'estudiantes'
    id = db.Column(db.Integer(), primary_key=True)
    nombres = db.Column(db.String(), nullable=False)
    apellidos = db.Column(db.String(), nullable=False)
    profesores = db.relationship('Profesor', secondary = 'profesores_estudiantes', lazy = 'dynamic')
    cursos = db.relationship('Curso', secondary = 'estudiantes_cursos', lazy = 'dynamic') # Relacion many

    def __init__ (self, id, nombres, apellidos, profesores, cursos):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos

class Profesor(db.Model):
    __tablename__ = 'profesores'
    id = db.Column(db.Integer(), primary_key=True)
    nombres = db.Column(db.String(), nullable=False)
    apellidos = db.Column(db.String(), nullable=False)
    estudiantes = db.relationship('Estudiante', secondary = 'profesores_estudiantes', overlaps="profesores")

    def __init__ (self, id, nombres, apellidos):
        self.id = id
        self.nombres = nombres
        self.apellidos = apellidos

# Crear tabla para relacion many-to-many entre Profesor y Estudiante
class ProfesorEstudiante(db.Model):
    __tablename__ = 'profesores_estudiantes'
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesores.id'), primary_key=True, nullable=False)
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiantes.id'), primary_key=True, nullable=False)
    promedio = db.Column(db.Float, nullable= False, default = 0)

    def __init__ (self, profesor_id, estudiante_id, promedio):
        self.profesor_id = profesor_id
        self.estudiante_id = estudiante_id
        self.promedio = promedio

class Curso(db.Model):
    __tablename__ = 'cursos'
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(), nullable=False)
    profesor_id = db.Column(db.Integer, db.ForeignKey('profesores.id'))
    extras = db.relationship('Extra', backref='cursos')
    estudiantes = db.relationship('Estudiante', secondary = 'estudiantes_cursos', lazy = 'dynamic', overlaps="cursos")

    def __init__ (self, id, nombres, profesor_id, extras, estudiantes):
        self.id = id
        self.nombres = nombres
        self.profesor_id = profesor_id

# Crear tabla para relacion many-to-many entre Estudiante y Curso
class EstudianteCurso(db.Model):
    __tablename__ = 'estudiantes_cursos'
    estudiante_id = db.Column(db.Integer, db.ForeignKey('estudiantes.id'), primary_key=True, nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'), primary_key=True, nullable=False)

    def __init__ (self, estudiante_id, curso_id):
        self.estudiante_id = estudiante_id
        self.curso_id = curso_id

class Extra(db.Model):
    __tablename__ = 'extras'
    nombre = db.Column(db.String(), primary_key=True, nullable=False)
    tema = db.Column(db.String(), primary_key=True, nullable=False)
    curso_id = db.Column(db.Integer, db.ForeignKey('cursos.id'))
    link = db.Column(db.String(), nullable=False)

    def __init__ (self, nombre, tema, curso_id, link):
        self.nombre = nombre
        self.tema = tema
        self.curso_id = curso_id
        self.link = link
'''
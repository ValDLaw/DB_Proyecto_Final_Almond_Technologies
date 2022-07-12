# DBP Proyecto 2: Almond Technologies

### Integrantes:

- Gian Franco Davila
- Sofía García
- Almendra Carrera
- Valeria Espinoza

## Información acerca de las librerías/frameworks/plugins utilizadas en Front-end, Back-end y Base de datos

### [Vue.js](https://vuejs.org/guide/introduction.html)

### [Flask](https://flask.palletsprojects.com/en/2.1.x/)

### [SQLAlchemy](https://docs.sqlalchemy.org/en/20/)

### [Flask-Login](https://flask-login.readthedocs.io/en/latest/)

### [JSON Web Tokens](https://jwt.io/)

### [Flask-Cors](https://flask-cors.readthedocs.io/en/latest/)

### [Werkzeug Security](https://werkzeug.palletsprojects.com/en/2.1.x/utils/)

### [Bulma.io](https://bulma.io/documentation/)

## Script para iniciar la base de datos con datos

```powershell
#entrar a usuario de psql
CREATE DATABASE almond_tec;
\c almond_tec
Se inicializa en el __init__.py los datos
```

## Información acerca de los API. Requests y Responses de cada endpoint utilizado en el sistema.

`/home`

Muestra la información general de la aplicación, con la oportunidad de dar feedback, es decir, lleva a un formulario de Google para recibir sugerencias.

`@app.route('/login', methods=['POST'])`

Permite al usuario iniciar sesión. Se debe pasar la autentificación de datos para poder redirigir al usuario a la ruta user. Si no, aparecen mensajes indicando lo que está mal. 

`@app.route('/signup', methods=['POST'])`

Ruta para poder crear una cuenta. Recibe los datos del formulario, y si no pasa la validación de datos muestra mensajes de advertencia. En caso todo este correcto, redirige a la persona a la ruta login .

`@app.route('/password', methods=['PATCH'])`

Permite al usuario poder modificar la contraseña en la base de datos si coloca sus datos correctamente.

### Las siguientes rutas sólo son visibles si se inicia sesión correctamente:

`@app.route ('/logout', methods=['POST'])`

Permite al usuario cerrar sesión al hacer click en el botón de logout.

`@app.route('/user', methods=['GET'])`

Permite ver el perfil del usuario que ha iniciado sesión.

`@app.route("/user/cursos", methods=["GET"])`

Muestra los cursos en los que el alumno está matriculado.

`@app.route("/user/cursos_disponibles", methods=["GET"])`

Le muestra al alumno los cursos disponibles a los que puede matricularse.

`@app.route("/user/cursos_ensenados", methods=["GET"])`

Muestra los alumnos inscritos en el curso dictado por el docente.

`@app.route("/matricular/<curso_id>", methods = ["GET"])`

Ruta que inscribe al alumno en el curso indicado. Las bases de datos se actualizan.

`@app.route("/abandonar/<curso_id>", methods = ["DELETE"])`

Permite al usuario abandonar el curso y eliminar su inscripción de las bases de datos.

`/tutoriales-main`

Muestra un menú con 4 opciones que son los diferentes tipos de aplicaciones que hay plataformas virtuales, videoconferencias, pizarras virtuales y apps de organización en los cuales redirecciona a la pagina de la categoria seleccionada

`/plataformas-virtuales-tutoriales`

Es una de los tipos de aplicación de tutoriales en la cual se muestran 4 plataformas virtuales con su respectiva descripción

`/videoconferencias-tutoriales`

Es una de los tipos de aplicación de tutoriales en la cual se muestran 4 aplicaciones de videoconferencias con su respectiva descripción

`/pizarras-virtuales-tutoriales`

Es una de los tipos de aplicación de tutoriales en la cual se muestran 9 aplicaciones de pizarras virtuales con su respectiva descripción

`/apps-organizacionales-tutoriales`

Es una de los tipos de aplicación de tutoriales en la cual se muestran 5 aplicaciones de organización con su respectiva descripción

`/Beneficios-main`

Se muestran 5 aplicaciones con su respectiva descripción, entre los cuales podemos encontrar: 3 empresas de tecnología que ofrecen descuentos para estudiantes y profesores; y 2 paginas en las cuales se pueden encontrar cursos y certificaciones para profesores gratuitas en diferentes ámbitos

`/modelo-de-clases`

En esta sección se muestran consejos y ayudas para estructurar una clase virtual segun la aplicacion que se seleccione

`/tips-main`

En este apartado se encuentran recomendaciones según el tipo de clases que la persona lleve, ya sean clases virtuales, híbridas o presenciales

`/material-adicional`

Muestra 3 apartados en los cuales se pueden escoger el tipo de aplicaciones que se desean ver que según la elección redirecciona a la página correspondiente

`/apps-participativa-ma`

Muestra 3 aplicaciones para volver más participativas las clases que permiten la interacción con los estudiantes

`/apps-temas-especificos-ma`

Muestran aplicaciones acerca de temas específicos en estos casos una especializada en programación( "sololearn") y una en matemáticas("iMathematics")

`/herramientas-digitales`

Similar al caso de tutoriales muestra 4 secciones con los tipos de aplicación que se pueden encontrar para redireccionar segun la eleccion a la página correspondiente

`/plataformas-virtuales-hd`

Es una de los tipos de aplicación de material adicional en la cual se muestran 4 plataformas virtuales con su respectiva descripción y link para poder utilizarlas

`/videoconferencias-hd`

Es una de los tipos de aplicación de material adicional en la cual se muestran 4 apps de videoconferencias con su respectiva descripción y link para poder utilizarlas.

`/pizarras-virtuales-hd`

Es una de los tipos de aplicación de material adicional en la cual se muestran 9 diferentes pizarras virtuales con su respectiva descripción y link para poder utilizarlas.

`/apps-organizacionales-hd`

Es una de los tipos de aplicación de material adicional en la cual se muestran 5 diferentes aplicaciones organizacionales con su respectiva descripción y link para poder ser utilizadas.

`/juegos-main`

Muestra 3 aplicaciones que permiten jugar mientras el alumno aprende temas específicos descritos debajo del nombre de la app.


## Host: Vue

## Forma de autenticación

Se utilizó JSON Web Token para la autentificación de los datos. Además se utilizaron otras funciones de *Werkzeug Security* o funciones propias para poder asegurar la seguridad de los datos del usuario.

## Manejo de errores HTTP:

Utilizando el código `@app.errorhandler(e)` de Flask, podemos manejar la respuesta que manda el API dependiendo del código de respuesta HTTP.

```python
@app.errorhandler(404) #not found
@app.errorhandler(401) #unauthorized (JWT)
@app.errorhandler(500) #internal server error
@app.errorhandler(405) #method not allowed (CORS)
@app.errorhandler(422) #unprocessable
```

### Errores en el Servidor (500)

Manejados por la función `abort()` de Flask, se llega allí con `try: … except: … `que ocurre en caso se marque el error como True. En este caso, se llama abort(500).

### Errores en el Cliente (400)

Se intentó construir la aplicación para prevenir el caso de que el cliente encuentre links o sea redirigido a páginas a las que no tiene acceso, pero en todo caso, este tipo de errores son manejados por `@token_required` de JWT y por Vue.js

### Redirección (300)

Manejado por Vue.js y `@token_required` de Flask-Login.

### Exitoso (200) & Informacional (100

Se ve el resultado de una operación exitosa en la terminal.

## Cómo ejecutar el sistema (Deployment scripts)

Ejecutar la API en Flask (windows):
```powershell
python -m venv virtualenv
virtualenv\Scripts\activate
pip install -r requirements.txt #sólo la 1ra vez

cd backend #entrar a la carpeta backend
$env:FLASK_APP = "server"
$env:FLASK_ENV = "development"
flask run
```

Ejecutar la página web en Vue:
```powershell
cd frontend_almondtec #entrar a esta carpeta
npm install #sólo la 1ra vez, para crear node_modules
yarn serve
```
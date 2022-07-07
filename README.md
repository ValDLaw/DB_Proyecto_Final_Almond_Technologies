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

### [Werkzeug Security](https://werkzeug.palletsprojects.com/en/2.1.x/utils/)

### [Bulma.io](https://bulma.io/documentation/)

## Script para iniciar la base de datos con datos

!!!!

## Información acerca de los API. Requests y Responses de cada endpoint utilizado en el sistema.

## Host: Vue

## Forma de autenticación

La librería *Flask-Login* es la principal herramienta de autenticación utilizada en nuestra aplicación, pero además se utilizaron otras funciones de *Werkzeug Security* o funciones propias para poder asegurar la seguridad de los datos del usuario.

## Manejo de errores HTTP:

Utilizando el código `@app.errorhandler(e)` de Flask, podemos manejar la respuesta que manda el API dependiendo del código de respuesta HTTP. 

### Errores en el Servidor (500)

Manejados por la función `abort()` de Flask, se llega allí con `try: … except: … `que ocurre en caso se marque el error como True. En este caso, se llama abort(500).

### Errores en el Cliente (400)

Se intentó construir la aplicación para prevenir el caso de que el cliente encuentre links o sea redirigido a páginas a las que no tiene acceso, pero en todo caso, este tipo de errores son manejados por `@login_required` de Flask-Login.

### Redirección (300)

Manejado por Vue.js y `@login_required` de Flask-Login.

### Exitoso (200) & Informacional (100

Se ve el resultado de una operación exitosa en la terminal.

## Cómo ejecutar el sistema (Deployment scripts)

`yarn serve`
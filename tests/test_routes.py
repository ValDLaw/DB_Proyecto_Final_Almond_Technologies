
def test_home_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_home_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post('/')
        assert response.status_code == 405
        assert b'Flask User Management Example!' not in response.data

def test_singup_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get('/signup')
        assert response.status_code == 200

def test_singup_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post('/signup')
        assert response.status_code == 405

def test_login_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get("/login")
        assert response.status_code == 200

def test_login_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post("/login")
        assert response.status_code == 405

def test_password_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get("/password")
        assert response.status_code == 200

def test_password_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post("/password")
        assert response.status_code == 405

def test_user_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get("/user")
        assert response.status_code == 200

def test_user_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post("/user")
        assert response.status_code == 405

def test_matricular_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get("/matricular")
        assert response.status_code == 200

def test_matricular_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post("/matricular")
        assert response.status_code == 405

def test_abandonar_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get("/abandonar")
        assert response.status_code == 200

def test_abandonar_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post("/abandonar")
        assert response.status_code == 405

def test_matricular_curso_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get("/matricular/<curso>")
        assert response.status_code == 200

def test_matricular_curso_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post("/matricular/<curso>")
        assert response.status_code == 405

def test_abandonar_curso_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get("/abandonar/<curso>")
        assert response.status_code == 200

def test_abandonar_curso_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post("/abandonar/<curso>")
        assert response.status_code == 405

def test_curso_dictado_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get("/dictado/<curso>")
        assert response.status_code == 200

def test_curso_dictado_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post("/dictado/<curso>")
        assert response.status_code == 405

def test_curso_matriculado_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get("/matriculado/<curso>")
        assert response.status_code == 200

def test_curso_matriculado_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post("/matriculado/<curso>")
        assert response.status_code == 405

def test_logout_get():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.get("/logout")
        assert response.status_code == 200

def test_logout_post():
    flask_app = create_app('flask_test.cfg')
    with flask_app.test_client() as test_client:
        response = test_client.post("/logout")
        assert response.status_code == 405
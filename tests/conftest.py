import pytest
from app import create_app

@pytest.fixture(scope='module')
def test_client():
    flask_app =  create_app('flask_test.cfg')
    with flask_app.test_client() as testing_client:
        yield testing_client

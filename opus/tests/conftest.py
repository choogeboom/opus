import pytest

from opus.app import create_app


@pytest.yield_fixture(scope='session')
def app():
    """
    Setup our flask app
    
    :return: 
    """
    params = {'DEBUG': False,
              'TESTING': True}

    _app = create_app(settings_override=params)

    context = _app.app_context()
    context.push()

    yield _app

    context.pop()


@pytest.yield_fixture(scope='function')
def client(app):
    """
    Set up an app client
    
    :param app: 
    :return: 
    """
    yield app.test_client()

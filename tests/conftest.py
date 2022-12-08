import pytest, socket, os

@pytest.fixture(scope="session")
def http_service():
    ip = socket.gethostbyname(socket.gethostname())
    port = os.getenv('PORT', default=8000)
    return "http://{}:{}/".format(ip, port)
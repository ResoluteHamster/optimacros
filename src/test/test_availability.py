import requests

HOST_ADDRESS = 'localhost'

def test_hello():
    res = requests.get(f'http://{HOST_ADDRESS}/hello_world')
    assert res.content.decode('utf-8') == '"Hello World"'



from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_main_route():
	response = client.get('/main')
	assert response.status_code == 200
	assert response.json() == {'message': 'Hey, good job! Good job!'}
	assert response.headers['content-type'] == 'application/json'


def test_test_route():
	response = client.get('/test')
	assert response.status_code == 200
	assert response.json() == {'message': 'Test route'}
	assert response.headers['content-type'] == 'application/json'

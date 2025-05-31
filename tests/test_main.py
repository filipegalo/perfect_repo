from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_main_route():
	response = client.get('/')
	assert response.status_code == 200
	assert response.json() == {'message': 'Hey, good job!'}


def test_main_route_returns_json():
	response = client.get('/')
	assert response.headers['content-type'] == 'application/json'

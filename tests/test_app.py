from main import app
from fastapi.testclient import TestClient
from transifex.clients.trivia_client import category_map
import json


client = TestClient(app)

def test_get_categories_endpoint():
    response = client.get("/get_categories/")
    assert response.status_code == 200
    assert response.json() == json.loads(json.dumps(category_map))


def test_create_resource_endpoint():
    categories = [15, 16]
    json = {
        "items": [{'category': category} for category in categories]
    }
    response = client.post('/create_resource/', json = json)
    data = response.json()
    errors = [d['data']['attributes']['errors'] for d in data]
    no_error = all(error == [] for error in errors)
    assert response.status_code == 200
    assert no_error == True

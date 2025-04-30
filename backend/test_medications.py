import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_get_medications(client):
    response = client.get('/medications')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_specific_medication(client):
    response = client.get('/medications/1')
    assert response.status_code == 200
    assert response.get_json()["medication_name"] == "Amoxicillin"

def test_add_medication(client):
    new_med = {
        "pet_id": 2,
        "medication_name": "Gabapentin",
        "dosage": "100mg",
        "frequency": "Once daily",
        "start_date": "2024-03-01",
        "end_date": "2024-03-10",
        "prescribed_by": "Dr. Taylor"
    }
    response = client.post('/medications', json=new_med)
    assert response.status_code == 201
    assert response.get_json()["message"] == "Mock medication added"

def test_update_medication(client):
    update_data = {
        "frequency": "Once a day"
    }
    response = client.put('/medications/1', json=update_data)
    assert response.status_code == 200
    assert response.get_json()["medication"]["frequency"] == "Once a day"

def test_delete_medication(client):
    response = client.delete('/medications/1')
    assert response.status_code == 200
    assert "deleted" in response.get_json()["message"].lower()
#
def test_get_medications_by_pet(client):
    response = client.get('/medications/pet/2')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

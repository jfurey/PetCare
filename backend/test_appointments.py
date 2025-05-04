import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()

def test_get_appointments(client):
    response = client.get("/appointments")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_add_appointment_missing_fields(client):
    response = client.post("/appointments", json={
        "pet_id": 1,
        "contact_id": 2,
        "appointment_type": "Veterinarian"
        # missing date and time
    })
    assert response.status_code == 400
    assert "Missing required fields" in response.get_json()["error"]

def test_add_appointment_invalid_type(client):
    response = client.post("/appointments", json={
        "pet_id": 1,
        "contact_id": 2,
        "appointment_type": "Surgery",
        "appointment_date": "2025-05-10",
        "appointment_time": "14:00:00"
    })
    assert response.status_code == 400
    assert "Invalid appointment_type" in response.get_json()["error"]

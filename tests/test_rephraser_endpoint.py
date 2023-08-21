import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

data = {
    "valid_a": {
        "text": "Sample input text to be rephrased.",
        "number_of_variants": 2
    },
    "invalid_a": {
        "text": "Sample input text to be rephrased.",
        "number_of_variants": -2
    },
    "invalid_b": {
        "text": "",
        "number_of_variants": 1
    }
}

def test_process_phrase_positive():
    request_data = {
        "text": "Sample input text to be rephrased.",
        "number_of_variants": 2
    }
    response = client.post("/rephrase", json=data.get("valid_a"))
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 2

def test_process_phrase_negative():
    response = client.post("/rephrase", json=data.get("invalid_a"))
    assert response.status_code == 422  # Unprocessable Entity

    error_detail = response.json()["detail"][0]["msg"]
    assert "Input should be greater than 0" in error_detail

    response = client.post("/rephrase", json=data.get("invalid_b"))
    assert response.status_code == 422  # Unprocessable Entity

    error_detail = response.json()["detail"][0]["msg"]
    assert "String should have at least 1 characters" in error_detail



if __name__ == "__main__":
    pytest.main()
# import pytest
# from app.main import app
# from fastapi.testclient import TestClient
# from unittest.mock import MagicMock, patch

# client = TestClient(app)

# data = {
#     "valid_a": {"text": "Sample input text to be rephrased.", "number_of_variants": 2},
#     "invalid_a": {
#         "text": "Sample input text to be rephrased.",
#         "number_of_variants": -2,
#     },
#     "invalid_b": {"text": "", "number_of_variants": 1},
# }

# TODO refactor

# @patch("app.dependencies.get_openai_client")
# def test_process_phrase_positive(mocked_openai_client):
#     openai_instance = MagicMock()
#     openai_instance.get_response.return_value = [
#         "Variant 1",
#         "Variant 2",
#     ]
#     mocked_openai_client.return_value = openai_instance

#     response = client.post("/rephrase", json=data.get("valid_a"))
#     assert response.status_code == 200
#     assert isinstance(response.json(), list)
#     assert len(response.json()) == 2

# @patch("app.dependencies.get_openai_client")
# def test_process_phrase_negative(mocked_openai_client):
#     openai_instance = MagicMock()
#     openai_instance.get_response.side_effect = ValueError("Invalid input")
#     mocked_openai_client.return_value = openai_instance

#     response = client.post("/rephrase", json=data.get("invalid_a"))
#     assert response.status_code == 422
#     assert "Input should be greater than 0" in response.text

#     response = client.post("/rephrase", json=data.get("invalid_b"))
#     assert response.status_code == 422
#     assert "String should have at least 1 characters" in response.text

# if __name__ == "__main__":
#     pytest.main()

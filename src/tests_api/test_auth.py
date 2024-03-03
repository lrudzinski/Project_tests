import requests
import pytest


TEST_URL = "https://restful-booker.herokuapp.com/auth"


@pytest.fixture
def test_data():
    return {"username": "admin", "password": "password123"}


def test_create_token_succes(test_data):
    response = requests.post(TEST_URL, json=test_data)
    assert response.status_code == 200
    assert "token" in response.json()


def test_create_token_not_succes(test_data):
    test_data["password"] = "BadBoy"
    response = requests.post(TEST_URL, json=test_data)
    assert response.status_code == 200
    assert "token" not in response.json()


if __name__ == "__main__":
    pytest.main()

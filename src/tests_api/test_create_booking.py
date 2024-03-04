import pytest
import requests

from config import TEST_URL


@pytest.fixture
def booking_data():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-03-01", "checkout": "2024-03-05"},
        "additionalneeds": "Breakfast",
    }


def test_create_booking_succes(booking_data):
    response = requests.post(TEST_URL, json=booking_data)

    assert response.ok
    assert "bookingid" in response.json()


def test_create_booking_not_success(booking_data):
    del booking_data["bookingdates"]
    response = requests.post(TEST_URL, json=booking_data)

    assert response.status_code == 500

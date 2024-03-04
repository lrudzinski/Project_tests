import pytest
import requests

from config import TEST_URL, get_authtoken


@pytest.fixture
def update_data():
    return {
        "firstname": "John",
        "lastname": "Smith",
        "totalprice": 211,
        "depositpaid": True,
        "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
        "additionalneeds": "Lunch",
    }


def test_update_booking(update_data):
    response_json = requests.get(TEST_URL)
    booking_id = response_json.json()[0]["bookingid"]
    response = requests.put(f"{TEST_URL}{booking_id}", json=update_data, cookies={"token": get_authtoken()})
    assert response.ok

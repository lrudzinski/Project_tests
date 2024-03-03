import pytest
import requests


@pytest.fixture
def update_data():
    return {
        "firstname": "John",
        "lastname": "Doe",
        "totalprice": 250,
        "depositpaid": True,
        "bookingdates": {"checkin": "2024-03-10", "checkout": "2024-03-15"},
        "additionalneeds": "Lunch",
    }


def test_update_booking():
    booking_id = requests.get("https://restful-booker.herokuapp.com/booking/").json()[0]["bookingid"]
    response = requests.put(f"https://restful-booker.herokuapp.com/booking/{booking_id}", json=update_data)
    assert response.ok

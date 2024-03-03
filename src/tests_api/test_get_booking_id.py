import pytest
import requests

TEST_URL = f"https://restful-booker.herokuapp.com/booking/"


def test_get_existing_booking():
    get_all_bookings = requests.get(f"{TEST_URL}").json()
    response = requests.get(f"{TEST_URL}{get_all_bookings[0]["bookingid"]}")
    assert response.ok
    booking = response.json()
    assert  booking


def test_get_nonexistent_booking():
    nonexistent_booking_id = "X"
    response = requests.get(f"{TEST_URL}{nonexistent_booking_id}")
    assert response.status_code == 404


if __name__ == "__main__":
    pytest.main()

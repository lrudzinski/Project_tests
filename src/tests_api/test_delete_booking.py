import pytest
import requests

TEST_URL = f"https://restful-booker.herokuapp.com/booking/"


def test_delete_booking():
    get_all_bookings = requests.get(f"{TEST_URL}").json()
    booking_id = get_all_bookings[0]["bookingid"]
    print(get_all_bookings)
    print(booking_id)
    response = requests.delete(f"{TEST_URL}{booking_id}")
    print(response)
    assert response.ok


if __name__ == "__main__":
    pytest.main()

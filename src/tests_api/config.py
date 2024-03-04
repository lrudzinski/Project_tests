import requests

URL_AUTH = "https://restful-booker.herokuapp.com/auth"
TEST_URL = "https://restful-booker.herokuapp.com/booking/"


def get_authtoken():
    return requests.post(URL_AUTH, json={"username": "admin", "password": "password123"}).json()["token"]

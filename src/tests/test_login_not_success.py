import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")
from src.dashboard_view import DashboardView
from src.login_view import LoginView
from selenium import webdriver

from pytest_bdd import scenarios, given, when, then, parsers

username = "Maslo@gmail.com"
password = "password1"
driver = webdriver.Chrome()
driver.maximize_window()
dash = DashboardView(driver)
login_page = LoginView(driver)


scenarios("features\\test_login_not_success.feature")


@given("the user is on the login page")
def step_user_on_login_page():
    dash.click_sign_in()


@when(parsers.parse("the user enters incorrect login credentials"))
def step_user_enters_incorrect_login_data():
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()


@then("the user is logged in successfully")
def step_user_logged_in_successfully():
    assert not login_page.validate_login()

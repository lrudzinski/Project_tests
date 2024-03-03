import sys, os
import time


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")
from src.dashboard_view import DashboardView
from src.register_view import RegisterView
from src.utils import generate_random_email
from selenium import webdriver

from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
dash = DashboardView(driver)
register_page = RegisterView(driver)


scenarios("features\\test_register_succes.feature")


@given("the user is on the register page")
def step_user_on_register_page():
    dash.click_sign_in()
    register_page.create_account(
        generate_random_email()
    )


@when(parsers.parse("the user enters correct register data"))
def step_user_enters_correct_register_data():
    register_page.click_radio_button("Mr")
    register_page.enter_first_name("Szczepan")
    register_page.enter_last_name("Borsuk")
    register_page.enter_new_password("password23")
    register_page.select_date_of_birth((10, 12, 2012))
    register_page.click_checkbox()
    register_page.click_register_button()


@then("the user is registered successfully")
def step_user_is_registered_successfully():
    assert register_page.is_register_succes()

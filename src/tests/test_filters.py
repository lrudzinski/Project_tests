import sys, os
import time


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")
from selenium import webdriver
from src.dashboard_view import DashboardView
from shop_view import ShopView
from pytest_bdd import scenarios, given, when, then, parsers


driver = webdriver.Chrome()
driver.maximize_window()
dash = DashboardView(driver)
shop = ShopView(driver)


scenarios("features\\test_filters.feature")


@given("the user choose category")
def step_user_choose_category():
    dash.show_category("Women")


@when(parsers.parse("the user filterying by Tops"))
def step_user_filterying_by_tops():
    shop.set_filter_by_checkbox_name("Tops")


@then("items shows according to filter")
def step_items_shows_according_to_filter():
    assert shop.get_filter_amount("Tops") == shop.get_amount_of_showing_items()

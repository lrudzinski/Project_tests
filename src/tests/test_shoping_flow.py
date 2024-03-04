import sys, os
import time

from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")
from selenium import webdriver

from dashboard_view import DashboardView
from login_view import LoginView
from shop_view import ShopView
from detail_view import DetailView
from summary_view import SummaryView
from pytest_bdd import scenarios, given, when, then, parsers
from address_view import AddressView
from shiping_view import ShipingView
from payment_view import PaymentView

username = "lizak2343333333333333333332234@gmail.com"
password = "password"
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
dash = DashboardView(driver)
login_page = LoginView(driver)
shop = ShopView(driver)
detail = DetailView(driver)
summmary = SummaryView(driver)
address = AddressView()
shiping = ShipingView()
payment = PaymentView()


scenarios("features\\test_shoping_flow.feature")


@given("1")
def step_user_on_login_page():
    dash.click_sign_in()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    dash.show_category("Women")


@when(parsers.parse("2"))
def step_user_enters_correct_login_data():
    items = shop.get_products()
    shop.get_details_of_product(items[0])
    detail.select_size("M")
    detail.select_size("L")
    detail.select_color("Blue")
    detail.add_to_cart()


@then("3")
def step_user_logged_in_successfully():
    assert True

@when(parsers.parse("2"))
def step_user_enters_correct_login_data():
    detail.select_size("M")
    detail.select_size("L")
    detail.select_color("Blue")
    detail.add_to_cart()
    detail.proceed_checkout_or_continue_shoping(True)


@then("3")
def step_user_logged_in_successfully():
    assert True

@when(parsers.parse("2"))
def step_user_enters_correct_login_data():
    summmary.enter_amount_product(10)
    summmary.proceed_proceed_checkout()

@then("3")
def step_user_logged_in_successfully():
    assert address.page_info == "SHOPPING-CART SUMMARY"

@when(parsers.parse("2"))
def step_user_enters_correct_login_data():
    address.enter_address("Dowton")
    address.enter_city("York")
    address.enter_phone_mobile(90000-535-35)
    address.enter_postcode(000000)
    address.select_state("Alabama")
    address.save_address()

@then("3")
def step_user_logged_in_successfully():
    assert address.page_info == "YOUR ADDRESSES"


@when(parsers.parse("2"))
def step_user_enters_correct_login_data():
    shiping.accept_agreement()
    shiping.proceed_proceed_checkout()

@then("3")
def step_user_logged_in_successfully():
    assert address.page_info == "Shipping"

@when(parsers.parse("2"))
def step_user_enters_correct_login_data():
    payment.payment_method("bankwire")
    payment.confirm_pay()

@then("3")
def step_user_logged_in_successfully():
    assert payment.is_pay_success()
    
    

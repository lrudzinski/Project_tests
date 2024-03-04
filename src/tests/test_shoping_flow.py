import sys, os


myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")
from selenium import webdriver

from utils import get_email_from_file
from dashboard_view import DashboardView
from login_view import LoginView
from shop_view import ShopView
from detail_view import DetailView
from summary_view import SummaryView
from pytest_bdd import scenarios, given, when, then, parsers
from address_view import AddressView
from shiping_view import ShipingView
from payment_view import PaymentView


driver = webdriver.Chrome()
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


@given("User login on Website and choose category")
def step_user_on_login_page():
    dash.click_sign_in()
    login_page.enter_username(get_email_from_file("email.txt")[0])
    login_page.enter_password("password23")
    login_page.click_login_button()
    dash.show_category("Women")


@when(parsers.parse("Choose item and change propereties of item"))
def step_user_choose_item_and_propereties():
    items = shop.get_products()
    shop.get_details_of_product(items[0])
    detail.select_size("M")
    detail.select_size("L")
    detail.select_color("Blue")
    detail.add_to_cart()


@when(parsers.parse("Go to summary, increase items amount and proceed checkout"))
def step_go_to_summary():
    summmary.enter_amount_product(10)
    summmary.proceed_proceed_checkout()


@when(parsers.parse("User enter address data"))
def step_user_enters_address_data():
    address.enter_address("Dowton")
    address.enter_city("York")
    address.enter_phone_mobile(90000-535-35)
    address.enter_postcode(000000)
    address.select_state("Alabama")
    address.save_address()



@when(parsers.parse("User accept agreement"))
def step_user_enters_accept_agreemen():
    shiping.accept_agreement()
    shiping.proceed_proceed_checkout()



@when(parsers.parse("User choose payment method"))
def step_user_choose_payment_method():
    payment.payment_method("bankwire")
    payment.confirm_pay()


@then("Payment successfull")
def step_payment_finish_successfully():
    assert payment.is_pay_success()
    
    

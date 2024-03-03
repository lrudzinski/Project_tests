from selenium.webdriver.common.by import By
from src.dashboard_view import DashboardView


class PaymentView(DashboardView):
    def __init__(self, driver):
        super().__init__(driver)
        self.pay_bankwire_button = (By.CLASS_NAME, "bankwire")
        self.pay_cheque_button = (By.CLASS_NAME, "cheque")
        self.button_confirm_pay = (By.CLASS_NAME, "btn btn-default button button-medium")

    def payment_method(self, option_pay):
        if option_pay == "bankwire":
            self.wait_for(self.pay_bankwire_button).click()
        if option_pay == "cheque":
            self.wait_for(self.pay_cheque_button).click()

    def confirm_pay(self):
        self.wait_for(self.button_confirm_pay).click()

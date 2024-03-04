from selenium.webdriver.common.by import By
from src.dashboard_view import DashboardView


class SummaryView(DashboardView):
    def __init__(self, driver):
        super().__init__(driver)
        self.button_proceed_checkout = (By.CLASS_NAME, "btn btn-default button button-medium")
        self.amount_product = (By.CLASS_NAME, "cart_quantity_input form-control grey")
        self.delete_product = (By.CLASS_NAME, "cart_quantity_delete")

    def enter_amount_product(self, amount_product):
        self.wait_for(self.amount_product).send_keys(amount_product)

    def remove_product(self):
        self.wait_for(self.delete_product).click()

    def proceed_proceed_checkout(self):
        self.wait_for(self.button_proceed_checkout).click()

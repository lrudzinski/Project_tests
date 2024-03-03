from selenium.webdriver.common.by import By
from src.dashboard_view import DashboardView


class ShipingView(DashboardView):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkbox_agreement_confirmation = (By.ID, "ecgv")
        self.button_proceed_checkout = (By.CLASS_NAME, "btn btn-default button button-medium")

    def remove_product(self):
        self.wait_for(self.checkbox_agreement_confirmation).click()

    def proceed_proceed_checkout(self):
        self.wait_for(self.button_proceed_checkout).click()

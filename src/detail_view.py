from selenium.webdriver.common.by import By
from dashboard_view import DashboardView
from selenium.webdriver.support.ui import Select


class DetailView(DashboardView):
    def __init__(self, driver):
        super().__init__(driver)
        self.product_status = (By.ID, "availability_value")
        self.button_add_to_cart = (By.CLASS_NAME, "exclusive added")
        self.button_proceed_checkout = (By.CLASS_NAME, "btn btn-default button button-medium")
        self.button_continue_shop = (By.CLASS_NAME, "continue btn btn-default button exclusive-medium")
        self.amount_product = (By.ID, "quantity_wanted")
        self.size = (By.XPATH, "//select[@id='group_1']")

    def enter_qoantity(self, amount):
        if self.check_stock_status():
            self.wait_for(self.find(self.amount_product)).send_keys(amount)
        return "Element  not visible"

    def select_size(self, size):
        dropdown = Select(self.wait_for(self.size))
        dropdown.select_by_visible_text(size)

    def select_color(self, color):
        self.wait_for((By.XPATH, f"//a[@name='{color}']")).click()

    def check_stock_status(self):
        if (
            self.wait_for(self.product_status).text
            == "This product is no longer in stock with those attributes but is available with others."
        ):
            return False
        elif self.wait_for(self.product_status).text == "In stock":
            return True

    def add_to_cart(
        self,
    ):
        print(self.check_stock_status())
        if self.check_stock_status():
            self.wait_for(self.button_add_to_cart)
        return "Element  not visible"


    def proceed_checkout_or_continue_shoping(self, choose):
        if choose is True:
            self.wait_for(self.find(self.button_proceed_checkout)).click()
        self.wait_for(self.find(self.button_continue_shop)).click()

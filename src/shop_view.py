import time
from selenium.webdriver.common.by import By
from dashboard_view import DashboardView
from utils import remove_text_and_convert_to_int


class ShopView(DashboardView):
    def __init__(self, driver):
        super().__init__(driver)
        self.products_list = (By.XPATH, "//a[@class='product_img_link']")
        self.filter = ""
        self.filters = (
            By.XPATH,
            f"//*[contains(@class, 'layered_filter')]//a[contains(text(), '{self.filter}')]",
        )
        self.filter_result = (
            By.XPATH,
            f"//*[contains(@class, 'layered_filter')]//a[contains(text(), '{self.filter}')]/span/text()",
        )
        self.items_amount = (By.CLASS_NAME, "product-count")

    def get_products(self):
        return self.find_many(self.products_list)

    def get_details_of_product(self, product):
        product.click()

    def set_filter_by_checkbox_name(self, checkbox_name):
        self.filter = checkbox_name
        self.wait_for(self.filters).click()
    
    def get_filter_amount(self, checkbox_name):
        time.sleep(10)
        self.filter = checkbox_name
        return remove_text_and_convert_to_int(self.wait_for(self.filters).text)


    def get_amount_of_showing_items(self):
        return remove_text_and_convert_to_int(self.wait_for(self.items_amount).text)

import os
import sys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + "/../")
from selenium.webdriver.common.by import By

from base_view import BaseView


class DashboardView(BaseView):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("http://www.automationpractice.pl/index.php?")
        self.login_link = (By.CLASS_NAME, "login")
        self.category = {
            "Women": (
                By.XPATH,
                "//a[@class='sf-with-ul' and contains(text(), 'Women')]",
            ),
            "Dresses": (
                By.XPATH,
                "//a[@class='sf-with-ul' and contains(text(), 'Dresses')]",
            ),
            "T-shirts": (
                By.XPATH,
                "//a[@class='sf-with-ul' and contains(text(), 'T-shirts')]",
            ),
        }

    def click_sign_in(self) -> None:
        self.wait_for(self.login_link).click()

    def show_category(self, category):
        self.wait_for(self.category[category]).click()

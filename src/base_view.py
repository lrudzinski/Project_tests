from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import Scroll


class BaseView(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.scroll = Scroll(driver)

    def wait_for(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_many(self, locator):
        return self.driver.find_elements(*locator)

    def swipe(self, direction: str, swipes: int = 1, duration: int = 500):
        if direction == "down":
            self.scroll.swipeDown(swipes, duration, self.driver)
        elif direction == "up":
            self.scroll.swipeUp(swipes, duration, self.driver)
        elif direction == "left":
            self.scroll.swipeLeft(swipes, duration, self.driver)
        elif direction == "right":
            self.scroll.swipeRight(swipes, duration, self.driver)
        else:
            raise KeyError("Swipe direction must be one of the following strings: 'down', 'up', 'left', 'right'")

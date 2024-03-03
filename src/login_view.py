from selenium.webdriver.common.by import By
from src.dashboard_view import DashboardView


class LoginView(DashboardView):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_textbox = (By.CSS_SELECTOR, "#email")
        self.password_textbox = (By.CSS_SELECTOR, "#passwd")
        self.login_button = (By.CSS_SELECTOR, "#SubmitLogin")
        self.login_succes = (By.CLASS_NAME, "info-account")

    def enter_username(self, username):
        self.wait_for(self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.wait_for(self.password_textbox).send_keys(password)

    def click_login_button(self):
        self.wait_for(self.login_button).click()

    def validate_login(self):
        try:
            self.wait_for(self.login_succes)
            return True
        except:
            return False

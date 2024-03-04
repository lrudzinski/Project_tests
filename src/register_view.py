from selenium.webdriver.common.by import By
from src.dashboard_view import DashboardView
from selenium.webdriver.support.ui import Select


class RegisterView(DashboardView):
    def __init__(self, driver):
        super().__init__(driver)
        self.create_email_texbox = (By.ID, "email_create")
        self.create_button = (By.ID, "SubmitCreate")
        self.radio_button_gender = {
            "Mr": (By.XPATH, f"//input[@id='id_gender1']"),
            "Ms": (By.XPATH, f"//input[@id='id_gender2']"),
        }
        self.first_name = (By.ID, "customer_firstname")
        self.last_name = (By.ID, "customer_lastname")
        self.new_password = (By.ID, "passwd")
        self.dropdown_date_birth = {
            "days": (By.ID, "days"),
            "months": (By.ID, "months"),
            "years": (By.ID, "years"),
        }
        self.checkbox_newsletter = (By.ID, "newsletter")
        self.register_button = (By.ID, "submitAccount")
        self.register_succes = (By.XPATH, "//p[@class='alert alert-success']")

    def create_account(self, email):
        self.wait_for(self.create_email_texbox).send_keys(email)
        self.wait_for(self.create_button).click()

    def click_radio_button(self, option: str) -> None:
        radio_button = self.wait_for(self.radio_button_gender[option])
        radio_button.click()

    def enter_first_name(self, first_name):
        self.wait_for(self.first_name).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.wait_for(self.last_name).send_keys(last_name)

    def enter_new_password(self, password):
        self.wait_for(self.new_password).send_keys(password)

    def select_date_of_birth(self, date_of_birth: tuple):
        dropdown = Select(self.wait_for(self.dropdown_date_birth["days"]))
        dropdown.select_by_value(str(date_of_birth[0]))
        dropdown = Select(self.wait_for(self.dropdown_date_birth["months"]))
        dropdown.select_by_value(str(date_of_birth[1]))
        dropdown = Select(self.wait_for(self.dropdown_date_birth["years"]))
        dropdown.select_by_value(str(date_of_birth[2]))

    def click_checkbox(self):
        self.wait_for(self.checkbox_newsletter).click()

    def click_register_button(self):
        self.wait_for(self.register_button).click()

    def is_register_succes(self):
        try:
            self.wait_for(self.register_succes)
            return True
        except:
            return False

from selenium.webdriver.common.by import By
from src.dashboard_view import DashboardView
from selenium.webdriver.support.ui import Select


class AddressView(DashboardView):
    def __init__(self, driver):
        super().__init__(driver)
        self.company = (By.ID, "company")
        self.address_1 = (By.ID, "address1")
        self.address_2 = (By.ID, "address2")
        self.city = (By.ID, "city")
        self.state = (By.ID, "id_state")
        self.postcode = (By.ID, "postcode")
        self.phone_home = (By.ID, "phone")
        self.phone_mobile = (By.ID, "phone_mobile")
        self.additional_info = (By.ID, "other")
        self.name_of_address = (By.ID, "alias")
        self.save_button = (By.ID, "submitAddress")

    def enter_company(self, company):
        self.wait_for(self.company).send_keys(company)

    def enter_address(self, address, address_2="None_second_address"):
        self.wait_for(self.address_1).send_keys(address)
        self.wait_for(self.address_2).send_keys(address_2)

    def enter_city(self, city):
        self.wait_for(self.city).send_keys(city)

    def select_state(self, state):
        dropdown = Select(self.wait_for(self.find(self.state)))
        dropdown.select_by_visible_text(state)

    def enter_postcode(self, postcode):
        self.wait_for(self.postcode).send_keys(postcode)

    def enter_phone_home(self, phone_home):
        self.wait_for(self.phone_home).send_keys(phone_home)

    def enter_phone_mobile(self, phone_mobile):
        self.wait_for(self.phone_mobile).send_keys(phone_mobile)

    def enter_additional_info(self, additional_info):
        self.wait_for(self.additional_info).send_keys(additional_info)

    def enter_name_of_address(self, name_of_address):
        self.wait_for(self.name_of_address).send_keys(name_of_address)

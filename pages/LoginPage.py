from elements.element_builder import ElementBuilder
from selenium.webdriver.common.by import By
from .BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__int__(driver)
        self.username_field = ElementBuilder(By.XPATH,"//*[@id=\"user-name\"]", driver)
        self.password_field = ElementBuilder(By.XPATH, "//*[@id=\"password\"]", driver)
        self.login_btn = ElementBuilder(By.XPATH,"//*[@id=\"login-button\"]",driver)

    def enter_username(self, keys):
        if self.username_field.element().is_element_visible():
            self.username_field.element().send_keys(keys)
        else:
            raise Exception("failed to enter email")

    def enter_password(self, keys):
        if self.password_field.element().is_element_visible():
            self.password_field.element().send_keys(keys)
        else:
            raise Exception("failed to enter password")

    def submit_login_form(self):
        if self.login_btn.element().is_element_visible() and self.login_btn.element().is_element_clickable():
            self.login_btn.element().click()
        else:
            raise Exception("failed to submit login form")
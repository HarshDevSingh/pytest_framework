from pages.LoginPage import LoginPage


class Pages:
    def __init__(self,driver):
        self.driver=driver

    def login_page(self):
        return LoginPage(self.driver)
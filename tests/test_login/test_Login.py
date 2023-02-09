from ..base_test import BaseTest


class TestLogin(BaseTest):

    def test_open_login(self):
        self.logger.info("test_open_login execution started", )
        self.pages.login_page().open()

    def test_login(self):
        self.logger.info("test_login execution started:")
        self.pages.login_page().open()
        self.pages.login_page().enter_username("standard_user")
        self.pages.login_page().enter_password("secret_sauce")
        self.pages.login_page().submit_login_form()

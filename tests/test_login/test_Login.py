from ..base_test import BaseTest
from utils.logging.Logger import Logger


class TestLogin(BaseTest):

    logger = Logger().logger()

    def test_open_login(self):
        self.logger.info("test_open_login execution started")
        self.pages.login_page().open()

    def test_login(self):
        self.logger.info("test_login execution started")
        self.pages.login_page().open()
        self.pages.login_page().enter_username("standard_user")
        self.pages.login_page().enter_password("secret_sauce")
        self.pages.login_page().submit_login_form()

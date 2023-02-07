import pytest
from ..base_test import BaseTest
from tests.get_pages import Pages


@pytest.mark.usefixtures("setup_driver")
class TestLogin(BaseTest):

    def test_open_login(self):
        pages = Pages(self.driver)
        pages.login_page().open()


    def test_login(self):
        pages = Pages(self.driver)
        pages.login_page().open()
        pages.login_page().enter_username("standard_user")
        pages.login_page().enter_password("secret_sauce")
        pages.login_page().submit_login_form()

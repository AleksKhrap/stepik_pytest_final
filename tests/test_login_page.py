from pages.login_page import LoginPage
import pytest


@pytest.mark.login_guest
@pytest.mark.parametrize("link", ["https://selenium1py.pythonanywhere.com/ru/accounts/login/"])
class TestGuestLoginPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link):
        self.login_page = LoginPage(browser, link)
        self.login_page.open()

    def test_that_login_link_is_correct(self):
        self.login_page.should_be_login_url()

    def test_guest_can_see_login_form(self):
        self.login_page.should_be_login_form()

    def test_guest_can_see_registration_form(self):
        self.login_page.should_be_register_form()

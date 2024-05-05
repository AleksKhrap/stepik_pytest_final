from pages.main_page import MainPage
import pytest


@pytest.mark.login_from_main_guest
@pytest.mark.parametrize("link", ["http://selenium1py.pythonanywhere.com/"])
class TestLoginFromMainPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link):
        self.main_page = MainPage(browser, link)  # иниц-ем Page Object, передаем в конструктор экземпляр драйвера
        self.main_page.open()

    def test_guest_can_go_to_login_page(self):
        self.main_page.go_to_login_page()
        """
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        """

    def test_guest_should_see_login_link(self):
        self.main_page.should_be_login_link()


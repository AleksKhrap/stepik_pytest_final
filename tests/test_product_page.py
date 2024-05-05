from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest
import time


@pytest.mark.product_guest
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  # "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/",
                                  # pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_"
                                  #             "207/?promo=offer7",
                                  #             marks=pytest.mark.xfail),
                                  ]
                         )
class TestGuestProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link):
        self.product_page = ProductPage(browser, link)
        self.product_page.open()

    # the-city-and-the-stars_95 при добавлении в корзину фэйлится из-за отсутствия алерта (это норма)
    # @pytest.mark.skip
    @pytest.mark.need_review
    def test_guest_can_add_product_to_basket(self):
        self.product_page.add_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.find_product_name()
        self.product_page.find_product_cost()

    # @pytest.mark.skip
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        self.product_page.add_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_not_be_success_message()

    # @pytest.mark.skip
    def test_guest_cant_see_success_message(self):
        self.product_page.should_not_be_success_message()

    # @pytest.mark.skip
    def test_message_disappeared_after_adding_product_to_basket(self):
        self.product_page.add_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.should_be_disappeared()

    # @pytest.mark.skip
    def test_guest_should_see_login_link_on_product_page(self):
        self.product_page.should_be_login_link()

    # @pytest.mark.skip
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self):
        self.product_page.go_to_login_page()

    # @pytest.mark.skip
    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        self.product_page.go_to_basket_page()
        self.basket_page = BasketPage(browser, browser.current_url)
        self.basket_page.is_basket_empty()
        self.basket_page.is_basket_empty_text_present()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.email = str(time.time()) + "@fakemail.org"
        self.password = "12576gJfr"
        self.login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        self.login_page.open()
        self.login_page.register_new_user(self.email, self.password)
        self.login_page.should_be_authorized_user()

        self.product_page = ProductPage(
            browser,
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        )
        self.product_page.open()

    def test_user_cant_see_success_message(self):
        self.product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        self.product_page.add_to_cart()
        self.product_page.solve_quiz_and_get_code()
        self.product_page.find_product_name()
        self.product_page.find_product_cost()

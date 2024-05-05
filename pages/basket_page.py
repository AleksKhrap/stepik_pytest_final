from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def is_basket_empty(self):
        try:
            self.browser.find_element(*BasketPageLocators.BASKET_ITEMS)
        except NoSuchElementException:
            return True
        return False

    def is_basket_empty_text_present(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE), "Basket is not empty"

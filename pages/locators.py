from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button[type='submit']")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button[type='submit']")
    ALERT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_page .product_main h1")
    ALERT_PRODUCT_COST = (By.CSS_SELECTOR, "#messages div:nth-child(3) .alertinner p strong")
    PRODUCT_COST = (By.CSS_SELECTOR,  ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")


class BasketPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")

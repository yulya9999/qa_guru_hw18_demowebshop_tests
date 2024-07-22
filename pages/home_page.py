import allure
from selene import browser, have
from tests.data.base_func import user_auth
from tests.data.base_params import LOGIN


class HomePage:

    def __init__(self):
        self.cookies = user_auth()

    @staticmethod
    @allure.step("Проверка авторизации")
    def check_login_auth():
        browser.all('.account').first.should(have.text(LOGIN))

    @allure.step("Переход в корзину")
    def open_to_cart(self):
        browser.all('.cart-label').first.click()
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': self.cookies})
        browser.driver.refresh()

        return self


home_page = HomePage()

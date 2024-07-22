import allure
import requests
from selene import browser, have
from tests.data.base_params import BASE_URL
from utils.attach import response_logging, response_attaching
from tests.data.base_func import user_auth


class CartPageAPI:
    def __init__(self):
        self.cookies = user_auth()

    def add_item_to_cart(self, item, info_item):
        with allure.step(f'Добавить товар "{info_item}" в корзину'):
            response = requests.post(url=f'{BASE_URL}/addproducttocart/catalog{item}',
                                     cookies={'NOPCOMMERCE.AUTH': self.cookies})
            response_logging(response)
            response_attaching(response)
            assert response.status_code == 200
        return self


class CartPageUI:
    def check_item_in_cart(self, info_item):
        with allure.step(f'Проверка наличия товара "{info_item}" в корзине'):
            browser.element('.cart-item-row .product').should(have.text(info_item))

        return self

    def check_quantity_item(self):
        with allure.step('Проверка количества товара в корзине'):
            browser.element('.qty-input').should(have.value("1"))
        return self

    def clean_cart(self):
        with allure.step('Очистка корзины'):
            browser.element('.remove-from-cart [type=checkbox]').click()
            browser.element('.common-buttons [name=updatecart]').click()

        return self


cart_page_api = CartPageAPI()
cart_page_ui = CartPageUI()

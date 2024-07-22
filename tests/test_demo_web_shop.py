import allure
from pages.home_page import home_page
from pages.cart_page import cart_page_ui, cart_page_api
from tests.data.base_params import code_book, code_phone, info_phone, info_book


@allure.feature("Тестирование сайта 'Demo Web Shop'")
@allure.story("Проверка наличия авторизации")
def test_check_login_auth():
    home_page.check_login_auth()


@allure.feature("Тестирование сайта 'Demo Web Shop'")
@allure.story("Добавление телефона в корзину")
def test_add_phone():
    cart_page_api.add_item_to_cart(code_phone, info_phone)
    home_page.open_to_cart()
    cart_page_ui.check_item_in_cart(info_phone)
    cart_page_ui.check_quantity_item()
    cart_page_ui.clean_cart()


@allure.feature("Тестирование сайта 'Demo Web Shop'")
@allure.story("Добавление книги в корзину")
def test_add_book():
    cart_page_api.add_item_to_cart(code_book, info_book)
    home_page.open_to_cart()
    cart_page_ui.check_item_in_cart(info_book)
    cart_page_ui.check_quantity_item()
    cart_page_ui.clean_cart()

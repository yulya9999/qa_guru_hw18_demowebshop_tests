import requests
from selene import browser
from tests.data.base_params import BASE_URL, LOGIN, PASS


def user_auth():
    data = {
        'Email': LOGIN,
        'Password': PASS
    }
    response = requests.post(url=f'{BASE_URL}/login', data=data, allow_redirects=False)
    cookie = response.cookies.get('NOPCOMMERCE.AUTH')
    return cookie


def open_browser():
    browser.open(BASE_URL)
    browser.driver.add_cookie({'name': "NOPCOMMERCE.AUTH", 'value': user_auth()})
    browser.driver.refresh()

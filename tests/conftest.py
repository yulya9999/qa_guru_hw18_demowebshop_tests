import pytest
from selene import browser
from tests.data.base_func import user_auth, open_browser
from dotenv import load_dotenv
import os


# @pytest.fixture(scope="session", autouse=True)
# def load_env():
#     load_dotenv()
#
#
# login_shop = os.getenv("LOGIN")
# pass_shop = os.getenv("PASS")


@pytest.fixture(scope="session", autouse=True)
def browser_params():
    browser.config.window_height = 1080
    browser.config.window_width = 1920
    user_auth()
    open_browser()

    yield
    browser.quit()

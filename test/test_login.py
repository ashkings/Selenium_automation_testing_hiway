import pytest, unittest, constant

from Utility.csv_loader import get_csv_data
from pages.open_hiway_url import OpenHighway
from pages.login_google import LoginUsingGoogle
from pages.driver import Driver
from pages.enter_login_credentials import LoginCredentials
from ddt import ddt, data, unpack


@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser")


@ddt
class TestLogin(unittest.TestCase):
    @pytest.yield_fixture()
    def setup(self, browser_name):
        driver = Driver(browser_name)
        global browser
        browser = driver.get_path()
        highway = OpenHighway(browser)
        highway.get_url()
        login_page = LoginUsingGoogle(browser)
        login_page.click_on_login()
        yield
        browser.close()

    @pytest.mark.usefixtures("setup")
    @data(*get_csv_data(constant.csv_path_for_successful_login))
    @unpack
    def test_successful_login(self, username, password):
        login_values = LoginCredentials(browser)
        login_values.enter_username(username)
        login_values.enter_password(password)


if __name__ == '__main__':
    pytest.main()

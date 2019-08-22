import pytest
import unittest
import constant
from Utility.csv_loader import get_csv_data
from pages.open_hiway_url import OpenHighway
from pages.login_google import LoginUsingGoogle
from pages.driver import Driver
from pages.enter_login_credentials import LoginCredentials
from pages.start_using_application import StartApplication
from ddt import ddt, data, unpack
import logging
import constant

Test_logger = logging.getLogger(__name__)
Test_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
file_handler = logging.FileHandler(constant.log_path_for_login)
file_handler.setFormatter(formatter)
Test_logger.addHandler(file_handler)

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
        page_access = StartApplication(browser)
        Test_logger.info("Reached to redirect login page")

        assert username in page_access.validating_access_of_user()
        Test_logger.info("Test passed successful")


if __name__ == '__main__':
    pytest.main()

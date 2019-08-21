import pytest
import unittest
from pages.open_hiway_url import OpenHighway
from pages.login_google import LoginUsingGoogle
from pages.driver import Driver
from pages.enter_login_credentials import LoginCredentials
from pages.start_using_application import StartApplication
from pages.timesheet import Timesheet


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
        login_values = LoginCredentials(browser)
        login_values.enter_username()
        login_values.enter_password()
        dashboard = StartApplication(browser)
        dashboard.click_on_start_using_button()
        global timesheet
        timesheet = Timesheet(browser)
        timesheet.click_on_timesheet()
        yield
        browser.close()

    @pytest.mark.usefixtures("setup")
    def test_timesheet_name_same_as_username(self):
        login_name = timesheet.get_logged_in_username()
        displayed_username = timesheet.get_name_on_timesheet()
        assert login_name.lower() in displayed_username


if __name__ == '__main__':
    pytest.main()

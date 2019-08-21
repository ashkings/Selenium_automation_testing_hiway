import pytest
import unittest
from pages.open_hiway_url import OpenHighway
from pages.login_google import LoginUsingGoogle
from pages.driver import Driver
from pages.enter_login_credentials import LoginCredentials
from pages.start_using_application import StartApplication
from pages.timesheet import Timesheet
from datetime import date, timedelta


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

    @pytest.mark.usefixtures("setup")
    def test_timesheet_loaded_in_todays_date(self):
        todays_date = date.today().strftime("%a, %b %d")
        timesheet_date = timesheet.get_date_on_timesheet()

        assert todays_date in timesheet_date

    @pytest.mark.usefixtures("setup")
    def test_next_button_disabled(self):
        todays_date = date.today().strftime("%a, %b %d")
        timesheet_date = timesheet.get_date_on_timesheet()
        if todays_date == timesheet_date:
            assert timesheet.next_button_state() is True

    @pytest.mark.usefixtures("setup")
    def test_prev_button_takes_a_day_back_on_click(self):
        for day in range(1, 3):
            prev_date = date.today() - timedelta(days=day)
            timesheet.click_prev_button()

            assert prev_date.strftime("%a, %b %d") in timesheet.get_date_on_timesheet()


if __name__ == '__main__':
    pytest.main()

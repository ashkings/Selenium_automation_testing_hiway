import pytest
import unittest
from pages.open_hiway_url import OpenHighway
from pages.login_google import LoginUsingGoogle
from pages.driver import Driver
from pages.enter_login_credentials import LoginCredentials
from pages.start_using_application import StartApplication
from pages.timesheet import Timesheet
from Utility.csv_loader import get_csv_data
from ddt import ddt, data, unpack
from datetime import date, timedelta
import constant
import logging

Test_logger = logging.getLogger(__name__)
Test_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
file_handler = logging.FileHandler(constant.log_path)
file_handler.setFormatter(formatter)
Test_logger.addHandler(file_handler)

@ddt
class TestTimesheet(unittest.TestCase):
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
        Test_logger.info("UserName  is fetched")

        displayed_username = timesheet.get_name_on_timesheet()
        Test_logger.info("Displayed UserName  is fetched from timesheet")

        assert login_name.lower() in displayed_username
        Test_logger.info("Test passed successful")

    @pytest.mark.usefixtures("setup")
    def test_timesheet_loaded_in_todays_date(self):
        todays_date = date.today().strftime("%a, %b %d")
        timesheet_date = timesheet.get_date_on_timesheet()
        Test_logger.info("Present date and Timesheet date fetched")

        assert todays_date in timesheet_date
        Test_logger.info("Test passed successful")

    @pytest.mark.usefixtures("setup")
    def test_next_button_disabled(self):
        todays_date = date.today().strftime("%a, %b %d")
        timesheet_date = timesheet.get_date_on_timesheet()
        Test_logger.info("Present date and Timesheet date fetched")

        if todays_date == timesheet_date:
            assert timesheet.next_button_state() is True
            Test_logger.info("Test passed successful")

    @pytest.mark.usefixtures("setup")
    def test_prev_button_takes_a_day_back_on_click(self):
        for day in range(1, 3):
            prev_date = date.today() - timedelta(days=day)
            timesheet.click_prev_button()

            assert prev_date.strftime("%a, %b %d") in timesheet.get_date_on_timesheet()
            Test_logger.info("Test passed successful")

    @pytest.mark.usefixtures("setup")
    @data(*get_csv_data(constant.csv_path_for_timesheet_data))
    @unpack
    def test_task_time_added_in_total_work_hrs(self, project_code, type, hrs, mins, desc):
        time_before_entry = timesheet.get_working_hrs_from_label()
        time_before_entry = (int(time_before_entry.split(':')[0]) * 60) + int(time_before_entry.split(':')[1])
        Test_logger.info("Time before Entry")


        timesheet.create_entry(project_code, type, hrs, mins, desc)

        time_after_entry = timesheet.get_working_hrs_from_label()
        time_after_entry = (int(time_after_entry.split(':')[0]) * 60) + int(time_after_entry.split(':')[1])
        Test_logger.info("Time after Entry")

        total_time = (time_after_entry - time_before_entry)
        assert total_time == (int(hrs) * 60 + int(mins))
        Test_logger.info("Test passed successful")

    @pytest.mark.usefixtures("setup")
    @data(*get_csv_data(constant.csv_path_for_color_data))
    @unpack
    def test_color_change_orange_to_blue_after_eight_hrs(self, project_code, type, hrs, mins, desc):
        timesheet.delete_entry()
        timesheet.create_entry(project_code, type, hrs, mins, desc)
        color_on_bar = timesheet.get_color_rgba_value()
        assert constant.orange_rgb == color_on_bar
        Test_logger.info("Bar color changed to orange")

        timesheet.create_entry()
        color_on_bar = timesheet.get_color_rgba_value()
        assert constant.blue_rgb == color_on_bar
        Test_logger.info("Test passed successful")

    @pytest.mark.usefixtures("setup")
    @data(*get_csv_data(constant.csv_path_for_color_data))
    @unpack
    def test_color_changes_to_pink_after_nine_hrs(self, project_code, type, hrs, mins, desc):
        timesheet.delete_entry()
        timesheet.create_entry(project_code, type, hrs, mins, desc)
        color_on_bar = timesheet.get_color_rgba_value()
        assert constant.orange_rgb == color_on_bar
        Test_logger.info("Bar color changed to orange")

        timesheet.create_entry()
        timesheet.create_entry()
        color_on_bar = timesheet.get_color_rgba_value()
        assert constant.pink_rgb == color_on_bar
        Test_logger.info("Test passed successful")

        if __name__ == '__main__':
            pytest.main()

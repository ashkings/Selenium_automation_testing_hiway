import pytest

from pages.open_hiway_url import OpenHighway
from pages.login_google import LoginUsingGoogle
from pages.driver import Driver
from pages.enter_login_credentials import LoginCredentials
from pages.start_using_application import StartApplication
from pages.timesheet import Timesheet
from ddt import ddt, file_data, unpack
import csv


@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.yield_fixture()
def setup(browser_name):
    driver = Driver(browser_name)
    global browser
    browser = driver.get_path()
    highway = OpenHighway(browser)
    highway.get_url()
    login_page = LoginUsingGoogle(browser)
    login_page.click_on_login()

@file_data('/home/ashu/Desktop/Selenium_Tracks/login.csv')
def test_login(username, password):
    login_values = LoginCredentials(browser)
    login_values.enter_username(username)
    login_values.enter_password(password)

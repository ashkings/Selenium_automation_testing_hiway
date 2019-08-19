import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from datetime import date
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


@pytest.yield_fixture()
def setup():
    global browser
    browser = webdriver.Chrome("/home/ashu/Desktop/Selenium_Tracks/web_drivers/chromedriver")
    browser.implicitly_wait(20)
    browser.maximize_window()
    browser.get("https://qa.hiway.hashedin.com")
    browser.find_element_by_link_text("LOGIN USING GOOGLE").click()
    browser.find_element_by_id("identifierId").send_keys("ashu.singla@hashedin.com")
    browser.find_element_by_id("identifierNext").click()
    browser.find_element_by_name("password").send_keys("Hashedin.com")
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "passwordNext")))
    browser.find_element_by_id("passwordNext").click()
    browser.find_element_by_class_name("btn").click()
    time.sleep(2)
    browser.find_element_by_xpath("//div/div[2]/span[4]/a").click()
    yield
    browser.close()


def test_name_on_timesheet_is_same_as_logged_in_user(setup):
    first_name = browser.find_element_by_class_name("username-position").text.split(".")[0]
    last_name = browser.find_element_by_class_name("username-position").text.split(".")[1].split("@")[0]
    username = first_name + " " + last_name
    displayed_first_name = browser.find_element_by_tag_name("h2").text.split(" ")[3]
    displayed_last_name = browser.find_element_by_tag_name("h2").text.split(" ")[4]
    displayed_username = displayed_first_name + " " + displayed_last_name
    assert username.lower() == displayed_username


def test_timesheet_loaded_in_todays_date(setup):
    todays_date = date.today().strftime("%a, %b %d")
    timesheet_date = browser.find_element_by_class_name("mobile-timesheet-date").text
    assert todays_date in timesheet_date

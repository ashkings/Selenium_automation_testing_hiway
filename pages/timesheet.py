from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Timesheet:
    # locators
    timesheet_button_xpath = "//a[@aria-label='Timesheet']"
    last_element_check_xpath = "//button[@ng-click='provideLeave()']"
    logged_username = 'username-position'
    timesheet_name = 'h2'
    date_class = 'mobile-timesheet-date'
    locator_next_button = "button[ng-click='next()']"
    locator_prev_button = "button[ng-click='prev()']"

    def __init__(self, driver):
        self.driver = driver

    def click_on_timesheet(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.last_element_check_xpath)))
        self.driver.find_element_by_xpath(self.timesheet_button_xpath).click()

    def get_logged_in_username(self):
        return self.driver.find_element_by_class_name(self.logged_username).text.split('@')[0].replace('.', ' ')

    def get_name_on_timesheet(self):
        return self.driver.find_element_by_tag_name(self.timesheet_name).text

    def get_date_on_timesheet(self):
        return self.driver.find_element_by_class_name(self.date_class).text

    def next_button_state(self):
        return self.driver.find_element_by_css_selector(self.locator_next_button).get_property('disabled')

    def click_prev_button(self):
        self.driver.find_element_by_css_selector(self.locator_prev_button).click()



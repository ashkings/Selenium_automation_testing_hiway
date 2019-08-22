from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import constant, time


class Timesheet:
    # locators
    timesheet_button_xpath = "//a[@aria-label='Timesheet']"
    last_element_check_xpath = "//button[@ng-click='provideLeave()']"
    logged_username = 'username-position'
    timesheet_name = 'h2'
    label_class = 'mobile-timesheet-date'
    locator_next_button = "button[ng-click='next()']"
    locator_prev_button = "button[ng-click='prev()']"
    project_code_dropdown = "input[type='search']"
    type_dropdown = "//md-select[@ng-model='newEntry.type']"
    locator_hrs = 'newEntry.hrs'
    locator_mins = 'newEntry.min'
    locator_desc = 'newEntry.description'
    locator_add = '//form/div[1]/button'
    locator_alert_div = 'div.md-toast-content'
    delete_button = '//md-icon-button/md-icon/i'
    s_no = '//form/div[1]/div[1]/div[1]/div[1]'
    color_bar = '.md-bar.md-bar2'

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
        return self.driver.find_element_by_class_name(self.label_class).text

    def next_button_state(self):
        return self.driver.find_element_by_css_selector(self.locator_next_button).get_property('disabled')

    def click_prev_button(self):
        self.driver.find_element_by_css_selector(self.locator_prev_button).click()

    def create_project_code(self, project_code):
        code = self.driver.find_element_by_css_selector(self.project_code_dropdown)
        code.clear()
        code.send_keys(project_code)

    def create_type(self, type):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, self.type_dropdown)))
        self.driver.find_element_by_xpath(self.type_dropdown).send_keys(type)

    def create_hrs(self, hrs):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, self.locator_hrs)))
        self.driver.find_element_by_name(self.locator_hrs).send_keys(hrs)

    def create_mins(self, mins):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.NAME, self.locator_mins)))
        self.driver.find_element_by_name(self.locator_mins).send_keys(mins)

    def create_description(self, desc):
        self.driver.find_element_by_name(self.locator_desc).send_keys(desc)

    def create_entry(self, project_code=constant.default_projectcode, type=constant.default_type,
                     hrs=constant.default_hrs, mins=constant.default_mins, desc=constant.default_desc):
        self.create_project_code(project_code)
        self.create_type(type)
        self.create_hrs(hrs)
        self.create_mins(mins)
        self.create_description(desc)

        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_add)))
        self.driver.find_element_by_xpath(self.locator_add).click()

        # Sleep used as page gonna refresh after every entry added so wait for it
        time.sleep(3)

    def get_working_hrs_from_label(self):
        return self.driver.find_element_by_class_name(self.label_class).text.split(' ')[0]

    def delete_entry(self):
        while True:
            try:
                self.driver.find_element_by_xpath(self.delete_button).click()
                self.wait_till_alert_goes()

            except NoSuchElementException:
                return

    def wait_till_alert_goes(self):
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_alert_div)))
        WebDriverWait(self.driver, 5).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.locator_alert_div)))

    def get_sno_from_timesheet_table(self):
        return str(self.driver.find_element_by_xpath(self.s_no).text)

    def get_color_rgba_value(self):
        return str(self.driver.find_element_by_css_selector(self.color_bar).value_of_css_property(
            'background-color'))

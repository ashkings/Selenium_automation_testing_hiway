from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


class LoginCredentials:
    def __init__(self, driver):
        self.driver = driver
        # locators
        self.id = 'identifierId'
        self.name = 'password'
        self.click_next_username_id = 'identifierNext'
        self.click_next_password_id = 'passwordNext'
        with open('/home/ashu/Desktop/Selenium_Tracks/login.csv', 'r') as file:
            list = csv.reader(file, delimiter=',')
            for row in list:
                if len(row) == 2:
                    self.username = row[0]
                    self.password = row[1]

    def enter_username(self):
        self.driver.find_element_by_id(self.id).send_keys(self.username)
        self.driver.find_element_by_id(self.click_next_username_id).click()

    def enter_password(self):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.NAME, self.name)))
        self.driver.find_element_by_name(self.name).send_keys(self.password)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, self.click_next_password_id)))
        self.driver.find_element_by_id(self.click_next_password_id).click()

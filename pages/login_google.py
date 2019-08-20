from selenium import webdriver
class LoginUsingGoogle:
    # locators
    link_text = "LOGIN USING GOOGLE"

    def __init__(self, driver):
        self.driver = driver

    def click_on_login(self):
        self.driver.find_element_by_link_text(self.link_text).click()

class LoginUsingGoogle:
    def __init__(self, driver):
        self.driver = driver
        self.link_text = 'LOGIN USING GOOGLE'

    def click_on_login(self):
        self.driver.find_element_by_link_text("LOGIN USING GOOGLE").click()

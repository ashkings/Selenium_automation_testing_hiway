class StartApplication:
    # locators
    btn = 'btn'
    tag = 'h3'

    def __init__(self, driver):
        self.driver = driver

    def click_on_start_using_button(self):
        self.driver.find_element_by_class_name(self.btn).click()

    def validating_access_of_user(self):
        return self.driver.find_element_by_tag_name(self.tag).text

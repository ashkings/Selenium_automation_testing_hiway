class StartApplication:
    def __init__(self, driver):
        self.driver = driver
        # locators
        self.btn = 'btn'

    def click_on_start_using_button(self):
        self.driver.find_element_by_class_name(self.btn).click()

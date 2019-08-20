class OpenHighway:
    def __init__(self, driver):
        self.driver = driver
        self.baseUrl = 'https://qa.hiway.hashedin.com'

    def get_url(self):
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)

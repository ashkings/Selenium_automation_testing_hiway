from selenium import webdriver


class Driver:
    def __init__(self, browser_name):
        if browser_name == 'Chrome':
            self.driver = webdriver.Chrome('/home/ashu/Desktop/Selenium_Tracks/web_drivers/chromedriver')
        elif browser_name == 'Firefox':
            self.driver = webdriver.Firefox(
                executable_path='/home/ashu/Desktop/Selenium_Tracks/web_drivers/geckodriver')

    def get_path(self):
        return self.driver

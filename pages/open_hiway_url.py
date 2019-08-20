from selenium import webdriver


class OpenUrl:
    baseUrl = 'https://qa.hiway.hashedin.com'

    def __init__(self, path="/home/ashu/Desktop/Selenium_Tracks/web_drivers/chromedriver"):
        self.browser = webdriver.Chrome(path)
        self.browser.implicitly_wait(20)
        self.browser.maximize_window()
        self.browser.get(self.baseUrl)

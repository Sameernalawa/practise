from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class baseclass:

    def __init__(self,driver):
        self.driver=driver

    def get_title(self):
        return self.driver.title

    def explicit_wait(self,timeout,locator):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))



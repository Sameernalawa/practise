from selenium.webdriver.common.by import  By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.CartPage import CartPage
from Utilities.BaseClass import baseclass


class ProductPage(baseclass):

    def __init__(self,driver):
        self.driver = driver
        super().__init__(driver)

        self.products = (By.XPATH, "//div[@class='card-block']")
        self.selectedItem_value = (By.CSS_SELECTOR, ".price-container")
        self.AddCart_button = (By.XPATH,"//a[contains(@class,'btn')]")


    def select_product(self):
        return self.driver.find_elements(*self.products)


    def price_text(self):
        self.explicit_wait(10,self.selectedItem_value)
        return self.driver.find_element(*self.selectedItem_value).text

    def Add_cart(self):
        self.driver.find_element(*self.AddCart_button).click()
        cartpage = CartPage(self.driver)
        return cartpage



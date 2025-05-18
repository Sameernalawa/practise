import json

import pytest
from selenium.webdriver.common.by import By

from Utilities.BaseClass import baseclass


class CartPage(baseclass):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        self.cartClick =  (By.XPATH, "//a[contains(text(),'Cart')]")
        self.cartText = (By.XPATH, "//h3[contains(text(), '790')]")
        self.placeorderButton = (By.XPATH, "//button[text()='Place Order']")
        self.name = (By.CSS_SELECTOR, "#name")
        self.country = (By.ID, "country")
        self.city = (By.ID, "city")
        self.card = (By.ID, "card")
        self.month = (By.ID, "month")
        self.year = (By.ID, "year")
        self.purchaseButton = (By.XPATH, "//button[@onclick='purchaseOrder()']")
        self.purchaseText = (By.XPATH, "//h2[text()='Thank you for your purchase!']")


    def cart(self):
        self.driver.find_element(*self.cartClick).click()
        return self.driver.find_element(*self.cartText).text



    def place_order(self,Name,Country,City,Card,Month,Year):

         self.driver.find_element(*self.placeorderButton).click()
         self.driver.find_element(*self.name).send_keys(Name)
         self.driver.find_element(*self.country).send_keys(Country)
         self.driver.find_element(*self.city).send_keys(City)
         self.driver.find_element(*self.card).send_keys(Card)
         self.driver.find_element(*self.month).send_keys(Month)
         self.driver.find_element(*self.year).send_keys(Year)
    def purchase(self):
        self.driver.find_element(*self.purchaseButton).click()
        return (self.driver.find_element(*self.purchaseText).text)

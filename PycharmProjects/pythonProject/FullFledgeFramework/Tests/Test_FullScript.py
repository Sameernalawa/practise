import json
import time
from logging import exception
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.ProductPage import ProductPage

def get_test_data():
    test_data_path = 'C:/Users/USER/PycharmProjects/pythonProject/FullFledgeFramework/TestData/Test_FullScript.json'
    with open(test_data_path) as f:
        test_data = json.load(f)
        return test_data["data"]

@pytest.mark.parametrize("test_list_item", get_test_data())
def test_ecommerce(setup,test_list_item):

    driver = setup
    product = ProductPage(driver)
    print(product.get_title())
    products = product.select_product()
    assert len(products) > 0
    print(len(products))
    for prod in products:
        mobile = prod.find_element(By.XPATH,"h4").text
        driver.execute_script("window.scrollBy(0, 500);")  # Scroll down by 500 pixels
        if mobile == "Iphone 6 32gb":
            prod.find_element(By.XPATH,"h4").click()
            break

    selected_price = product.price_text()
    print("this is selected value",selected_price)
    cartpage = product.Add_cart()
    time.sleep(1)
    alert_text = driver.switch_to.alert
    print(alert_text.text)
    alert_text.accept()
    time.sleep(1)
    cart_value = cartpage.cart()
    print(cartpage.get_title())
    print("this is cart value",cart_value)
    assert  cart_value  in selected_price
    cartpage.place_order(test_list_item["Name"], test_list_item["Country"], test_list_item["City"], test_list_item["Card"], test_list_item["Month"], test_list_item["Year"])

    purchase_text = cartpage.purchase()
    print(purchase_text)

    driver.save_screenshot("finalConfirmation.png")













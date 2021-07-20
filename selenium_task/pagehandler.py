from re import search
from sys import maxsize
from time import time
import pywinauto
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import (
    UnexpectedAlertPresentException,
    NoSuchElementException,
    StaleElementReferenceException,
    ElementNotVisibleException,
    WebDriverException,
    TimeoutException,
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

#Creating driver variable and install ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

#Opening Google Browser
def open_google(website):
    driver.get(website)
    #driver.maximize_window()
    time.sleep(0.5)

def agree_terms():
    terms = driver.find_element_by_id("L2AGLb")
    terms.click()

def navigate_to_yahoo_finance():
    to_search = driver.find_element_by_name("q")
    to_search.clear()
    to_search.send_keys("Yahoo Finance")
    time.sleep(0.5)
    to_search.send_keys(Keys.RETURN)

def click_link_to_yahoo():
    driver.find_element_by_class_name("yuRUbf").click()
    time.sleep(0.5)
   
def agree_yahoo_terms():
    driver.find_element_by_name("agree").click()
    time.sleep(1)

def choose_topic(topic):
   search_topic = driver.find_element_by_id("yfin-usr-qry")
   search_topic.clear()
   search_topic.send_keys(topic)
   search_topic.send_keys(Keys.RETURN)
   time.sleep(1)

def current_tesla_price():
    try:
        price_per_share = driver.find_element_by_css_selector("#quote-header-info > div > div > div > div > div > div > span[data-reactid='31']")
        print(price_per_share.text)
    except:
        print("No element founded!!")
        driver.close()

def close_browser():
    print("See you later!")
    driver.close()
#
#
#price_per_share = driver.find_element_by_css_selector("#quote-header-info > div > div > div > span[data-reactid='35']")
####REMEBER###write some comments to functions.

if __name__ == "__main__":
    open_google("https://www.google.com/")
    agree_terms()
    navigate_to_yahoo_finance()
    click_link_to_yahoo()
    agree_yahoo_terms()
    choose_topic("Tesla")
    current_tesla_price()
    close_browser()
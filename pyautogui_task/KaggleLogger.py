from logging import log
from sys import maxsize
from time import time
import pyperclip
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
###################imports###########################

#Creating driver variable and install ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

#Opening website
def open_website(website):
    driver.get(website)
    driver.maximize_window()
    time.sleep(0.5)

#Agree website all terms
def agree_terms():
    terms = driver.find_element_by_id("L2AGLb")
    terms.click()

#Google search to Kaggle
def navigate_to_kaggle():
    to_search = driver.find_element_by_name("q")
    to_search.clear()
    to_search.send_keys("kaggle")
    time.sleep(0.5)
    to_search.send_keys(Keys.RETURN)

def click_link():
    driver.find_element_by_class_name("yuRUbf").click()
    time.sleep(1)
    driver.find_element_by_link_text("Sign In").click()

#Signing up into Kaggle
def sign_up_with_google(email_address, email_last_part, password):
    time.sleep(0.5)
    pyautogui.click(x=913, y=402)
    time.sleep(2)
    pyautogui.write(email_address, interval= 0.08)
    pyperclip.copy("@")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.write(email_last_part, interval= 0.08)
    pyautogui.press('enter')
    ###password section####
    time.sleep(2)
    pyautogui.write(password, interval= 0.08)
    pyautogui.press('enter')

############function calls##############
open_website("https://www.google.com/")
agree_terms()
navigate_to_kaggle()
click_link()
    # - - - - - - - --  First part of email - End part of email.
sign_up_with_google("seleniummarkkanen", "gmail.com", "Kunkkupulla12!")


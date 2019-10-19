from selenium import webdriver
import pyautogui
import time
import autopy

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()

    context.browser.get('http://bg-ddordzo-01/dzo/#/home/pruzaociUsluga')
    time.sleep(1.5)

    context.browser.find_element_by_id('username').click()
    pyautogui.typewrite('dcirovic')

    context.browser.find_element_by_id('password').click()
    pyautogui.typewrite('1234asdf')

    context.browser.find_element_by_id('login').click()
    time.sleep(1.5)

def after_all(context):

    context.browser.quit()

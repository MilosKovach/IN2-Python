from selenium import webdriver
import time

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(5)
    context.browser.maximize_window()

def before_feature(context, feature):
    if 'login' in feature.tags:
        pass
    else:
        context.browser.get('http://bg-ddordzo-01/dzo/#/home')
        context.browser.find_element_by_id('username').send_keys('dcirovic')
        context.browser.find_element_by_id('password').send_keys('1234asdf')
        context.browser.find_element_by_id('login').click()
        time.sleep(1)

def after_all(context):
    context.browser.quit()

#LOGIN BEZ GRESKE



import os
import webbrowser
import pyautogui
import time
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



driver=webdriver.firefox
driver.maximize_window()
driver.get('http://bg-ddordzo-01/dzo/#/session')

time.sleep(1)

id='username'
btn=driver.find_element_by_id(id)
btn.click()


pyautogui.typewrite ('dcirovic')
pyautogui.press('enter')

csss='password'
btnn=driver.find_element_by_id(csss)
btnn.click()
pyautogui.typewrite('1234asdf')

lgn='login'
btnn1=driver.find_element_by_id(lgn)
btnn1.click()

time.sleep(2)
try:
    greska = driver.find_element_by_xpath('/html/body/app-root/p-growl/div/div/div/div[2]/p')
    os.system("notepad.exe Greska404.txt")
except NoSuchElementException:
    os.system('notepad.exe Greska403.txt')



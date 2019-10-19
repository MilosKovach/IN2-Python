# Login korisnika sa ogranicenim pristupom
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

#LOGIN BEZ GRESKE


driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://bg-ddordzo-01/dzo/#/session')

time.sleep(1)

id='username'
btn=driver.find_element_by_id(id)
btn.click()


pyautogui.typewrite ('jpejin')
pyautogui.press('enter')

csss='password'
btnn=driver.find_element_by_id(csss)
btnn.click()
pyautogui.typewrite('1234asdf')

lgn='login'
btnn1=driver.find_element_by_id(lgn)
btnn1.click()
time.sleep(1)

try:
    pristup=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dashboard/div/div/p/b')
    time.sleep(1)
    os.system('notepad.exe Greska406.txt')
    time.sleep(0.5)
except NoSuchElementException:
    os.system('notepad.exe Greska405.txt')




#Test padajuceg menija

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
from collections import Counter



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

time.sleep(2)
try:
    lista =driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul')
    items = lista.find_elements_by_tag_name("li")
    if (len(items) > 1):
        os.system('notepad.exe Greska407.txt')
    else:
        os.system("notepad.exe Greska408.txt")
except:
    NoSuchElementException
    os.system("notepad.exe Greska408.txt")

#pretraga po tekstu
#driver.find_elements_by_xpath("//*[contains(text(), 'Nemate pravo pristupa nijednom')]")

#odredjivanje velicine liste
#  lista =driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul')
 # items = lista.find_elements_by_tag_name("li")
#   if (len(items) > 1):
#      os.system('notepad.exe Greska407.txt')
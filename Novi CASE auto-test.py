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
from bs4 import BeautifulSoup
import arrow
import pyperclip

print('Unesite USERNAME')
user=input()
print('Unesite SIFRU')
sifra=input()
print('Unesite JMBG Korisnika')
JMBG_Korisnika=input()


driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://bg-ddordzo-01/dzo/#/session')

time.sleep(1)

id='username'
btn=driver.find_element_by_id(id)
btn.click()


pyautogui.typewrite (user)
pyautogui.press('enter')

csss='password'
btnn=driver.find_element_by_id(csss)
btnn.click()
pyautogui.typewrite(sifra)

lgn='login'
btnn1=driver.find_element_by_id(lgn)
btnn1.click()

time.sleep(1)

osiguranici=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[2]')
osiguranici.click()
time.sleep(0.5)

ocisti=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/div/p-button[2]/button')
ocisti.click()

osiguraniciJMBG=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/div/span[1]/input')
osiguraniciJMBG.click()
pyautogui.typewrite(JMBG_Korisnika)
time.sleep(1)



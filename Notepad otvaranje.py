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


driver=webdriver.Chrome()
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

clas='#topbar-icons > a:nth-child(3) > span.topbar-icon.fa.fa-sign-out'
clasbtn=driver.find_element_by_css_selector(clas)
clasbtn.click()
time.sleep(1)



id='username'
btn=driver.find_element_by_id(id)
btn.click()


pyautogui.typewrite('jpejin',)
pyautogui.press('enter')


csss='password'
btnn=driver.find_element_by_id(csss)
btnn.click()
time.sleep(1)
pyautogui.typewrite('1234asdf',)

lgn='login'
btnn1=driver.find_element_by_id(lgn)
btnn1.click()

time.sleep(1)




if x=dr


while x is True
    os.system('notepad Greska404.txt')
else
    os.system('notepad Greska403.txt')

x=driver.find_element('Nemate pravo')
print('x')

#try:
    #driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-dashboard > div > div > p > b')

   # return os.system('notepad Greska404.txt')

   # except
   # NoSuchElementException

   # return False

   #if element=('driver.find_element_by_partial_link_text("Nemate pravo")')

#except NoSuchElementException:
#elif
   # os.system('notepad Greska403.txt')


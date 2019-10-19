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

clas='#topbar-icons > a:nth-child(3) > span.topbar-icon.fa.fa-sign-out'
clasbtn=driver.find_element_by_css_selector(clas)
clasbtn.click()
time.sleep(1)



id='username'
btn=driver.find_element_by_id(id)
btn.click()


pyautogui.typewrite('dcirovic',)
pyautogui.press('enter')

csss='password'
btnn=driver.find_element_by_id(csss)
btnn.click()
pyautogui.typewrite('1234asdf',)

lgn='login'
btnn1=driver.find_element_by_id(lgn)
btnn1.click()

time.sleep(1)

osiguranici=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-dashboard > div > div > p-card:nth-child(1) > div > div > div > div > div.card > span')
osiguranici.click()

time.sleep(1)
pocetna=driver.find_element_by_css_selector('body > app-root > app-home > div > div.sidebar > p-scrollpanel > div > div.ui-scrollpanel-wrapper > div > div > app-menu > div > ul > ul > li:nth-child(1) > a')
pocetna.click()

time.sleep(1)
dokumenta=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-dashboard > div > div > p-card:nth-child(2) > div > div > div > div > div.card > h3')
dokumenta.click()
time.sleep(1)
pocetna=driver.find_element_by_css_selector('body > app-root > app-home > div > div.sidebar > p-scrollpanel > div > div.ui-scrollpanel-wrapper > div > div > app-menu > div > ul > ul > li:nth-child(1) > a')
pocetna.click()
time.sleep(1)
pruzaoci_usluga=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-dashboard > div > div > p-card:nth-child(3) > div > div > div > div > div.card > h3')
pruzaoci_usluga.click()

time.sleep(1)
pocetna=driver.find_element_by_css_selector('body > app-root > app-home > div > div.sidebar > p-scrollpanel > div > div.ui-scrollpanel-wrapper > div > div > app-menu > div > ul > ul > li:nth-child(1) > a')
pocetna.click()
time.sleep(1)
cenovnici=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-dashboard > div > div > p-card:nth-child(4) > div > div > div > div > div.card')
cenovnici.click()

time.sleep(1)
pocetna=driver.find_element_by_css_selector('body > app-root > app-home > div > div.sidebar > p-scrollpanel > div > div.ui-scrollpanel-wrapper > div > div > app-menu > div > ul > ul > li:nth-child(1) > a')
pocetna.click()
time.sleep(1)
poredjenje_usluga=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-dashboard > div > div > p-card:nth-child(5) > div > div > div > div > div.card')
poredjenje_usluga.click()


time.sleep(1)
pocetna=driver.find_element_by_css_selector('body > app-root > app-home > div > div.sidebar > p-scrollpanel > div > div.ui-scrollpanel-wrapper > div > div > app-menu > div > ul > ul > li:nth-child(1) > a')
pocetna.click()
time.sleep(1)
administracija=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-dashboard > div > div > p-card:nth-child(6) > div > div > div > div > div.card')
administracija.click()


time.sleep(1)
pocetna=driver.find_element_by_css_selector('body > app-root > app-home > div > div.sidebar > p-scrollpanel > div > div.ui-scrollpanel-wrapper > div > div > app-menu > div > ul > ul > li:nth-child(1) > a')
pocetna.click()

time.sleep(1)

time.sleep(1)


#from selenium.common.exceptions import NoSuchElementException

#elements=driver.find_elements_by_partial_link_text("Greška")
#if not elements:
 #   print("No element found")
#else:
 #   element = elements[0]
  #  print("F O U N D")

#elements=driver.find_element_by_css_selector('body > app-root > p-growl > div > div > div')
#if not elements:
 #   os.system("notepad.exe Greska404.txt")
#else:
 #   os.system("notepad.exe Greska403.txt")

#try:
 #   element=driver.find_element_by_partial_link_text('Nemate pravo pristupa nijednom delu aplikacije')
#except NoSuchElementException:
 #   os.system("notepad.exe Greska403.txt")
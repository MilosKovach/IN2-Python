#UBACIVANJE ELEMENTA ADMINISTRATOR!!!

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


driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://bg-ddordzo-01/dzo/#/home/administracija/uloge')


time.sleep(1)

id='username'
btn=driver.find_element_by_id(id)
btn.click()


pyautogui.typewrite ('bcadovski')
pyautogui.press('enter')

csss='password'
btnn=driver.find_element_by_id(csss)
btnn.click()
pyautogui.typewrite('1234asdf')

lgn='login'
btnn1=driver.find_element_by_id(lgn)
btnn1.click()

time.sleep(2)


bttn=driver.find_elements_by_xpath("//*[contains(text(), 'Administrator')]")
bttn[0].click()
bttn1 = driver.find_elements_by_css_selector("span[class='ui-button-icon-left ui-clickable pi pi-search']")

for element in bttn1:
    if(element.is_displayed()):
        element.click()
        break
time.sleep(1)

pregled=driver.find_elements_by_xpath("//*[contains(text(), 'Pregled PU - meni')]")
pregled[0].click()
time.sleep(1)
dodaj_dugme=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-uloge-details/div[2]/div/p-picklist/div/div[2]/div/button[1]/span[1]')
dodaj_dugme.click()
time.sleep(1)

sacuvaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-uloge-details/div[2]/p-button/button/span[2]')
sacuvaj.click()
time.sleep(4)
#element_present = EC.element_to_be_clickable((By.CSS_SELECTOR, '#topbar-icons > a:nth-child(3) > span.topbar-icon.fa.fa-sign-out'))
#WebDriverWait(driver, 10).until(element_present)

#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((driver.find_element_by_css_selector,'#topbar-icons > a:nth-child(3) > span.topbar-icon.fa.fa-sign-out')))

logout=driver.find_element_by_css_selector('#topbar-icons > a:nth-child(3) > span.topbar-icon.fa.fa-sign-out')
logout.click()
time.sleep(1)


id='username'
btn=driver.find_element_by_id(id)
btn.click()


pyautogui.typewrite ('bcadovski')
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
    greska = driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dashboard/div/div/p-card[3]/div/div/div/div/div[2]')
    os.system("notepad.exe Greska511.txt")
except:
    vrati_nazad=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-uloge-details/div[2]/div/p-picklist/div/div[2]/div/button[3]/span[2]')
    vrati_nazad.click()

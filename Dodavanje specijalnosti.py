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

time.sleep(1)


sifrarnici=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[7]/a/i[1]')
sifrarnici.click()
time.sleep(0.5)

specijalnosti=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[7]/ul/ul/li[3]/a/i')
specijalnosti.click()
time.sleep(1)

dodaj=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-specijalnost-list > div > app-sifarnik-table > div > p-button.ng-star-inserted > button > span.pi.pi-plus.ui-clickable.ui-button-icon-left.ng-star-inserted')
dodaj.click()

time.sleep(1)

Naziv=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-specijalnost-list/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]')
Naziv.click()
pyautogui.typewrite('Opsesivno kompulsivni poremecaj')
time.sleep(1)


sacuvaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-specijalnost-list/div/app-sifarnik-table/p-dialog[1]/div/div[3]/p-footer/button[1]/span[1]')
sacuvaj.click()
time.sleep(3)

dodaj_opet=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-specijalnost-list > div > app-sifarnik-table > div > p-button.ng-star-inserted > button > span.pi.pi-plus.ui-clickable.ui-button-icon-left.ng-star-inserted')
dodaj_opet.click()

time.sleep(1)

Naziv_aubapecijalnosti=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-specijalnost-list/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]')
Naziv_aubapecijalnosti.click()
pyautogui.typewrite('Bezrazlozan strah kradje podataka')
time.sleep(2)


pyautogui.press('tab')
time.sleep(1)
pyautogui.typewrite('Ops')
time.sleep(2)

oppsesivno=driver.find_element_by_xpath('/html/body/div[2]/ul/li[1]')
oppsesivno.click()

sacuvaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-specijalnost-list/div/app-sifarnik-table/p-dialog[1]/div/div[3]/p-footer/button[1]/span[1]')
sacuvaj.click()
time.sleep(3)

osvezi=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-specijalnost-list/div/div/p-button[1]/button/span[1]')
osvezi.click()

time.sleep(2)

pretraga1=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-specijalnost-list/div/div/span[1]/input')
pretraga1.click()

time.sleep(1)
pyautogui.typewrite('Bez')
time.sleep(2)

klikni=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-specijalnost-list/div/app-sifarnik-table/p-table/div/div/table/tbody/tr/td[2]')
klikni.click()
time.sleep(1)

info=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-specijalnost-list/div/app-sifarnik-table/p-table/div/div/table/tbody/tr/td[6]/div/button[1]/span[1]')
info.click()

time.sleep(1)


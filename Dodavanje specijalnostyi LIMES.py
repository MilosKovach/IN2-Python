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

pruzaoci_usluga=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-dashboard > div > div > p-card:nth-child(3) > div > div > div > div > div.card')
pruzaoci_usluga.click()
time.sleep(1)

nazivpretraga=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/span[2]/input')
nazivpretraga.click()
pyautogui.typewrite('LIMES SOFT')
time.sleep(2)

klikni_na_LIMES=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[2]')
klikni_na_LIMES.click()

detaljnije=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[8]/div/button[1]/span[1]')
detaljnije.click()
time.sleep(1)

specijalnosti=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/div[2]/p-tabmenu/div/ul/li[2]/a/span[2]')
specijalnosti.click()
time.sleep(1)

dodaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-specijalnosti-pu/div/app-sifarnik-table/div/p-button[1]/button/span[2]')
dodaj.click()
time.sleep(1)

dodavanje_specijalnosti=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-specijalnosti-pu/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]/p-autocomplete/span/input')
dodavanje_specijalnosti.click()
pyautogui.typewrite('Gastro')

time.sleep(2)

padajuci_meni_specijalnosti=driver.find_element_by_xpath('/html/body/div[2]/ul/li')
padajuci_meni_specijalnosti.click()
time.sleep(1)

doktori=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-specijalnosti-pu/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/input')
doktori.click()
pyautogui.typewrite('Dr Nele Karajlic')

sacuvaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-specijalnosti-pu/div/app-sifarnik-table/p-dialog[1]/div/div[3]/p-footer/button[1]/span[2]')
sacuvaj.click()
time.sleep(2)


pruzaoci_usluga1=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[3]/a/span')
pruzaoci_usluga1.click()
time.sleep(1)

ocisti=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/p-button[2]/button/span[2]')
ocisti.click()
time.sleep(1)

specijalnosti_pretraga=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/span[6]/p-autocomplete/span/input')
specijalnosti_pretraga.click()
pyautogui.typewrite('Gastro')
time.sleep(1)
Padajuci=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/span[6]/p-autocomplete/span/div/ul/li/span')
Padajuci.click()
time.sleep(1)

ulaz_u_PU=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[2]')
ulaz_u_PU.click()
time.sleep(1)


detaljnije1=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[8]/div/button[1]')
detaljnije1.click()
time.sleep(1)
predji_na_specijalnost=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/div[2]/p-tabmenu/div/ul/li[2]/a')
predji_na_specijalnost.click()
time.sleep(1)

obelezi_specijalnost=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-specijalnosti-pu/div/app-sifarnik-table/p-table/div/div/table/tbody/tr/td[1]/span[2]')
obelezi_specijalnost.click()
time.sleep(1)
info=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-specijalnosti-pu/div/app-sifarnik-table/p-table/div/div/table/tbody/tr/td[3]/div/button[1]/span[1]')
info.click()

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


pu=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[3]/a/span')
pu.click()

time.sleep(1)

ocisti=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/p-button[2]/button/span[2]')
ocisti.click()

time.sleep(2)

naziv=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/span[2]/input')
naziv.click()
pyautogui.typewrite('LIMES')
time.sleep(2)

polje=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[2]')
polje.click()
time.sleep(1)

detaljnije=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[8]/div/button[1]/span[1]')
detaljnije.click()
time.sleep(1)

radnovreme=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/div[2]/p-tabmenu/div/ul/li[3]/a/span[2]')
radnovreme.click()
time.sleep(1)

dodaj_radnovreme=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/div[2]/p-tabmenu/div/ul/li[3]/a/span[2]')
dodaj_radnovreme.click()
time.sleep(1)

radnidan=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/div/p-button[1]/button')
radnidan.click()
time.sleep(1)


radnidan1=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]/p-dropdown/div/label')
radnidan1.click()
time.sleep(1)

radnimdanima=driver.find_element_by_xpath('/html/body/div[2]/div/ul/li[2]/span')
radnimdanima.click()
time.sleep(2)

radiOD=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-inputmask/input')
radiOD.click()
pyautogui.typewrite('0900')
time.sleep(1)

radiDO=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-inputmask/input')
radiDO.click()
pyautogui.typewrite('1700')
time.sleep(1)

sacuvaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[3]/p-footer/button[1]/span[2]')
sacuvaj.click()
time.sleep(2)

pu1=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[3]/a')
pu1.click()
time.sleep(1)

obrisi=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/p-button[2]/button/span[2]')
obrisi.click()
time.sleep(2)

naziv_pretraga=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/span[2]/input')
naziv_pretraga.click()
pyautogui.typewrite('LIMES')
time.sleep(2)

udji_u_LIMES=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[2]')
udji_u_LIMES.click()
time.sleep(1)

detalji=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[8]/div/button[1]/span[1]')
detalji.click()
time.sleep(1)

try:
    radi=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/div[1]/div[1]/div[12]/div')
    print('OTVOREN JE CUVENI LIMES')
except NoSuchElementException:
    print('NE RADI NAS DRAGI LIMES')




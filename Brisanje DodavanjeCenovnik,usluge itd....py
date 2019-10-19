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
import subprocess

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



cenovnici_cena=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[4]/a')
cenovnici_cena.click()
time.sleep(1)

Naziv_usluge=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/div/span[1]/input')
Naziv_usluge.click()
pyautogui.typewrite('Lobotomus ParaExtraOrdinarus')

time.sleep(2)

try:
    udji_u_stavku=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/app-cenovnik-table/p-table/div/div/table/tbody/tr/td[2]/span[2]')
    udji_u_stavku.click()
    time.sleep(1)
    udjidetalji=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/app-cenovnik-table/p-table/div/div/table/tbody/tr[1]/td[6]/div/button[1]/span[1]')
    udjidetalji.click()

    time.sleep(1)

    obelezistavku=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-details/div/div[2]/app-usluga-pu/div/app-usluga-pu-table/p-table/div/div/table/tbody/tr/td[2]')
    obelezistavku.click()
    time.sleep(1)
    brisanjestavke=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-details/div/div[2]/app-usluga-pu/div/app-usluga-pu-table/p-table/div/div/table/tbody/tr/td[10]/div/button[4]')
    brisanjestavke.click()
    time.sleep(1)

    potvrdi12=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-details/div/div[2]/app-usluga-pu/div/app-usluga-pu-table/p-confirmdialog/div/div[3]/button[1]/span[2]')
    potvrdi12.click()
    time.sleep(1)
except NoSuchElementException:
    print('Nema elementa usluge')


cenovnici_cena=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[4]/a')
cenovnici_cena.click()
time.sleep(1)

ocisti=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/div/p-button[2]/button/span[1]')
ocisti.click()

time.sleep(2)

try:
    Naziv_usluge=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/div/span[1]/input')
    Naziv_usluge.click()
    pyautogui.typewrite('Lobotomus ParaExtraOrdinarus')

    time.sleep(2)

    brisanje=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/app-cenovnik-table/p-table/div/div/table/tbody/tr/td[6]/div/button[5]/span[1]')
    brisanje.click()
    time.sleep(1)

    potvrdi11=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/app-cenovnik-table/p-confirmdialog/div/div[3]/button[1]/span[2]')
    potvrdi11.click()

    time.sleep(1)
except NoSuchElementException:
    print('Nema elementa usluge')

time.sleep(1)
sifrarnici=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[7]/a/i[1]')
sifrarnici.click()
time.sleep(1)

usluge=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[7]/ul/ul/li[4]/a/i')
usluge.click()

time.sleep(1)
pretraganaziva=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-usluga-list/div/div/span[1]')
pretraganaziva.click()
time.sleep(1)

pyautogui.typewrite('Kontrola rada centralnog')
time.sleep(2)
try:
    pretraga=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-usluga-list/div/app-sifarnik-table/p-table/div/div/table/tbody/tr/td[2]/span[2]')
    pretraga.click()
    delete=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-usluga-list/div/app-sifarnik-table/p-table/div/div/table/tbody/tr/td[5]/div/button[3]')
    delete.click()
    potvrdi=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-usluga-list/div/app-sifarnik-table/p-confirmdialog/div/div[3]/button[1]/span[1]')
    potvrdi.click()
    time.sleep(1)
except NoSuchElementException:
    print('Nema elementa usluge')

cenovnici=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[4]/a/i')
cenovnici.click()
time.sleep(1)
pretraga_cenovnika=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/div/span[1]')
pretraga_cenovnika.click()
pyautogui.typewrite('Lobotomus ParaExtraOrdinarus')
time.sleep(3)


try:
    pretraga_cenovnika=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/app-cenovnik-table/p-table/div/div/table/tbody/tr/td[2]/span[2]')
    pretraga_cenovnika.click()
    delete_cenovnik=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/app-cenovnik-table/p-table/div/div/table/tbody/tr/td[6]/div/button[5]')
    delete_cenovnik.click()
    potvrdi_brisanje_cenovnika=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-list/div/app-cenovnik-table/p-confirmdialog/div/div[3]/button[1]/span[1]')
    potvrdi_brisanje_cenovnika.click()
    time.sleep(1)
except NoSuchElementException:
    time.sleep(1)
    print('Nema elementa cenovnika')
time.sleep(1)

pruzaoci_usluga=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[3]/a/i')
pruzaoci_usluga.click()
time.sleep(1)

pretraga_naziva=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/span[2]/input')
pretraga_naziva.click()
pyautogui.typewrite('LIMES SOFT')
time.sleep(3)

try:
    pretraga_pruzaoca_usluga=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr[1]/td[2]')
    pretraga_pruzaoca_usluga.click()
    delete_pruzaoca_usluga=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr[1]/td[8]/div/button[4]/span[1]')
    delete_pruzaoca_usluga.click()
    potvrdi_brisanje_pruzaoca_usluga=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-confirmdialog/div/div[3]/button[1]')
    potvrdi_brisanje_pruzaoca_usluga.click()
    time.sleep(1)
except NoSuchElementException:
    time.sleep(1)
    print('Nema elemenata pruzaoca usluga')
time.sleep(1)

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

osiguranici=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-dashboard > div > div > p-card:nth-child(1) > div > div > div > div > div.card')
osiguranici.click()
time.sleep(1)

ocisti=driver.find_elements_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/div/p-button[2]/button')
ocisti.click()
time.sleep(1)

JMBG_osiguranika=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/div/span[1]/input')
JMBG_osiguranika.click()
pyautogui.typewrite('1801949810')
time.sleep(2)

osiguranik_gizela=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/app-osiguranik-table/p-table/div/div/table/tbody/tr')
osiguranik_gizela.click()

detaljnije=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/app-osiguranik-table/p-table/div/div/table/tbody/tr/td[7]/div/button[1]')
detaljnije.click()
time.sleep(1)

osigurani_slucajevi=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/div[2]/p-tabmenu/div/ul/li[2]/a/span[2]')
osigurani_slucajevi.click()
time.sleep(1)

otvori_novi_sluvaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/div/p-button[1]/button/span[1]')
otvori_novi_sluvaj.click()
time.sleep(1)

polisa_osiguranja=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]/p-autocomplete/span/button')
polisa_osiguranja.click()
time.sleep(2)

ime_osiguranika=driver.find_element_by_xpath('/html/body/div[3]/ul/li[1]/span')
ime_osiguranika.click()
time.sleep(1)

Identifikacija=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-dropdown/div/div[3]')
Identifikacija.click()
time.sleep(1)
LK=driver.find_element_by_xpath('/html/body/div[3]/div/ul/li[1]')
LK.click()

Komentar=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]')
Komentar.click()
pyautogui.typewrite('Zali se na ostar bol u grudima, najverovatnije izazvan opstipacijom i losom ishranom')
time.sleep(1)

sacuvaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-dialog[1]/div/div[3]/p-footer/button[1]')
sacuvaj.click()
time.sleep(1)

Polisa_osiguranja=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-table/div/div/table/tbody/tr/td[2]')
Polisa_osiguranja.click()

detaljnije=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-table/div/div/table/tbody/tr/td[6]/div/button[1]')
detaljnije.click()
time.sleep(1)

otvori_novi_dokument=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/div/p-splitbutton/div/button[2]')
otvori_novi_dokument.click()

standardni_uput=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/div/p-splitbutton/div/div/ul/li[1]/a/span')
standardni_uput.click()
time.sleep(1)

pruzalac_usluga=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]/p-autocomplete')
pruzalac_usluga.click()
pyautogui.typewrite('Euromed')
time.sleep(2)

padajuci_meni=driver.find_element_by_xpath('/html/body/div[3]/ul')
padajuci_meni.click()
time.sleep(1)

komentar_otvaranja=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/textarea')
komentar_otvaranja.click()
pyautogui.typewrite('Ucestvovao u takmicenju u prejedanju i sad se zali na bolove')

sacuvajopet=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/p-dialog[1]/div/div[3]/p-footer/button[1]')
sacuvajopet.click()
time.sleep(1)

obelezi_uput=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/p-table/div/div/table/tbody/tr/td[2]')
obelezi_uput.click()

detaljnijeopet=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/p-table/div/div/table/tbody/tr/td[13]/div/button[1]')
detaljnijeopet.click()
time.sleep(1)

dodaj2=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/div/p-button[1]/button')
dodaj2.click()
time.sleep(1)

stavka_cenovnika=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-autocomplete/span/input')
stavka_cenovnika.click()
pyautogui.typewrite('Specijal')
time.sleep(1)

klik=driver.find_element_by_xpath('/html/body/div[3]/ul/li[7]')
klik.click()
time.sleep(1)

vreme=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-inputmask')
vreme.click()
pyautogui.typewrite('1145')
time.sleep(1)

doktor=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[4]/div[2]/input')
doktor.click()
pyautogui.typewrite('Dr Nele Karajliic')

pokrice=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[5]/div[2]/p-autocomplete/span/button')
pokrice.click()
pyautogui.typewrite('Dijagnost')
time.sleep(1)

MR11=driver.find_element_by_xpath('/html/body/div[3]/ul/li[1]')
MR11.click()
time.sleep(1)

sacuvaj11=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[3]/p-footer/button[1]')
sacuvaj11.click()










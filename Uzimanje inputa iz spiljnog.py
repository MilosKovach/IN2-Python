import os
import webbrowser
import pyautogui
import time
import selenium
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import json

'''''
print('Unesite USERNAME')
user=input()
print('Unesite SIFRU')
sifra=input()
#print('Unesite JMBG Korisnika')
#JMBG_Korisnika=input()
'''''''''


driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://bg-ddordzo-01/dzo/#/sessioni')

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


#
# wb2 = load_workbook('C:\\LISTA_JMBG_TEST1.xlsx')
# sh = wb2.active

# osiguranici=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[2]')
# osiguranici.click()
# time.sleep(1)
# jmbgpretraga=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/div/span[1]/input')
# jmbgpretraga.click()

with open("C:\\Users\milosk\Desktop\podaci.json") as input_file:
 data = json.load(input_file)

 for row in data:
   try:
    JMBG = row['osiguranikJmbg']

    #Excel fajl
    # JMBG=(sh.cell(i+2,1).value)
    # JMBG=str(JMBG)

    # Osiguranici Meni

    driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[2]').click()

    time.sleep(1)

    ocistiopet=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/div/p-button[2]/button')
    ocistiopet.click()
    jmbgpretraga123 = driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/div/span[1]/input')
    jmbgpretraga123.click()

    JMBG_osiguranika = driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/div/span[1]/input')
    JMBG_osiguranika.click()
    pyautogui.typewrite(JMBG)
    time.sleep(1)
    izaberiosiguranika=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/app-osiguranik-table/p-table/div/div/table/tbody/tr/td[1]')
    izaberiosiguranika.click()
    detaljnije=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik/div/app-osiguranik-table/p-table/div/div/table/tbody/tr/td[7]/div/button[1]')
    detaljnije.click()
    time.sleep(1)
    osiguranislucajevi=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/div[2]/p-tabmenu/div/ul/li[2]/a/span[2]')
    osiguranislucajevi.click()
    otvorinovislucaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/div/p-button[1]/button')
    otvorinovislucaj.click()
    time.sleep(1.33)
    try:

     polisaosiguranja=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]/p-autocomplete/span/button')
     polisaosiguranja.click()
     time.sleep(2)
     polisaElement = driver.find_elements_by_class_name ("ui-autocomplete-list-item")
     polisaElement[0].click()
    except :
          print(row['nosilacPolise'] + ' Nema vazecu polisu osiguranja')
          continue

    identifikacija21=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-dropdown/div/div[3]')
    identifikacija21.click()

    isprava=driver.find_elements_by_class_name('ui-dropdown-item')
    isprava[0].click()
    IME = row['komentarOtvaranje']

    komentarotvaranja=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/textarea')
    komentarotvaranja.click()
    pyautogui.typewrite(IME)

    sacuvaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-dialog[1]/div/div[3]/p-footer/button[1]')
    sacuvaj.click()
    time.sleep(2)
    print('osiguranik ' + row['nosilacPolise'] + ' je prosao kako treba')
   except:
    print('doslo je do greske kod ' + row['nosilacPolise'] + ' osiguranika')

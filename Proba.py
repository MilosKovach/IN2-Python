from selenium.webdriver.common.keys import Keys
import os
 import webbrowser
 import pyautogui
 import time
 import selenium
 from selenium.webdriver.support.ui import WebDriverWait
 from selenium.webdriver.common.by import By
 from selenium.webdriver.support import expected_conditions as EC
 from selenium import webdriver
 from selenium.webdriver.support.ui import WebDriverWait
 from selenium.webdriver.support import expected_conditions as EC
 from selenium.webdriver.common.by import By
 from selenium.common.exceptions import TimeoutException
 from collections import Counter
 from bs4 import BeautifulSoup
 import arrow
 import pandas as pd
 import xlrd
 import openpyxl
 import json
 from pprint import pprint
 from openpyxl import Workbook
 from openpyxl import load_workbook
 import bs4 as bs

with open("C:\\Users\milosk\Desktop\Adrese.json") as input_file:
 dataAddress = json.load(input_file)


link1=dataAddress['appAddress']+'#/session'
link2=dataAddress['appAddress']+'#/home/osiguranici/osiguraniSlucaj/'

driver=webdriver.Chrome()
driver.maximize_window()
driver.get(link1)


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

with open("C:\\Users\milosk\Desktop\Pokrice.json") as input_file:
 data = json.load(input_file)


   try:

    driver.get(link2+row['osId']+ '/dokumenti/' + row['dokId'])
    time.sleep(1)

    pokricaosiguranja=driver.find_element_by_xpath('//*[@id="ui-accordiontab-0"]/span[2]')
    pokricaosiguranja.click()
    time.sleep(1)
    nazivpokrica=driver.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/div/span[1]/input')
    nazivpokrica.click()
    pyautogui.typewrite(row['nazivPokrica'])
    time.sleep(1)

    izaberiNP=driver.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[1]/div/span')
    izaberiNP.click()


    span_element = driver.find_element_by_xpath ('//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[8]/div/span')
    rezervisaniIznos=float(span_element.text)
    print(rezervisaniIznos)


    DodajStavku=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/div/p-button[1]/button')
    DodajStavku.click()
    time.sleep(1)

    StavkaCenovnika=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-autocomplete/span/button')
    StavkaCenovnika.click()
    pyautogui.typewrite(row['stavkaCenovnika'])
    time.sleep(1.33)

    izaberistavku=driver.find_element_by_xpath('/html/body/div[2]/ul/li/span')
    izaberistavku.click()
    time.sleep(0.5)

    termin=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-inputmask/input')
    termin.click()
    pyautogui.typewrite('1234')
    time.sleep(0.5)

    #doktor=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[4]/div[2]/input')
    #doktor.click
    #pyautogui.typewrite('Dr Dragan David Dabic')
    #time.sleep(0.5)

    pokrice=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[5]/div[2]/p-autocomplete/span/input')
    pokrice.click()
    pyautogui.typewrite(row['nazivPokrica'])
    time.sleep(1)

    izaberipokrice=driver.find_element_by_xpath('/html/body/div[2]/ul/li/span')
    izaberipokrice.click()
    time.sleep(0.5)

    sacuvaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[3]/p-footer/button[1]')
    sacuvaj.click()

    time.sleep(1)

    # otvoripokrica1=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/p-accordion/div/p-accordiontab/div[1]')
    # otvoripokrica1.click()
    # time.sleep(1)
    #
    ocisti1=driver.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/div/p-button[2]/button/span[1]')
    ocisti1.click()
    time.sleep(0.5)


    nazivpokrica1 = driver.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/div/span[1]/input').send_keys(Keys.HOME)
    nazivpokrica1.click()
    pyautogui.typewrite(row['nazivPokrica'])
    time.sleep(1)

    rezervisanavrednostobelezi=driver.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[1]/div')
    rezervisanavrednostobelezi.click()

    span_element = driver.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[8]/div/span')
    rezervisaniIznosNOVI = float(span_element.text)
    print(rezervisaniIznosNOVI)
    if  (rezervisaniIznos+row['iznosEur']<=rezervisaniIznosNOVI and rezervisaniIznos+row['iznosEur'] + 0.01>=rezervisaniIznosNOVI):
        print('Uspesno je rezervisan iznos za novi pregled')

    else:
        print('Something went wrong')





   except NoSuchElementException:
       print('123456789"')
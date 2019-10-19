from behave import *
import selenium.webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException


import pyautogui
use_step_matcher("re")

pokrice = {'rezervisaniIznos': 0, 'id': 0}
novopokrice = {'NoviIznos':0}


@given("postoji osiguranik sa ID brojem (?P<ID_OSIGURANIKA>.+)")
def ID_BR_OSIGURANIKA(context, ID_OSIGURANIKA):
    context.browser.get('http://bg-ddordzo-01/dzo/#/home/osiguranici/'+ID_OSIGURANIKA)
    pokrice['rezervisaniIznos'] = 5

@step("postoji dokument sa ID brojem (?P<ID_DOK>.+)")
def ID_BR_Dokumenta(context, ID_DOK):
    try:
        context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/div[2]/p-tabmenu/div/ul/li[2]').click()

        WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,
            '/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-table/div/div/table/tbody/tr[1]/td[2]')))

        context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-table/div/div/table/tbody/tr[1]/td[2]').click()
        context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-table/div/div/table/tbody/tr[1]/td[6]/div/button[1]/span[1]').click()
        context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/p-table/div/div/table/tbody/tr/td[8]/span[2]').click()
        context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/p-table/div/div/table/tbody/tr/td[13]/div/button[1]/span[1]').click()
    except NoSuchElementException:
        print('Ne postoji korisnik sa ovim podacima')

@step("postoji pokriće sa nazivom (?P<ID_POKRICA>.+)")
def ID_Pokrica(context, ID_POKRICA):
    pauza='//*[@id="ui-accordiontab-'+ str(pokrice['id'])+'-content"]/div/app-pokrice-osiguranika/div/div/span[1]/input'
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/p-accordion/div/p-accordiontab/div[1]')))
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/p-accordion/div/p-accordiontab/div[1]').click()
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,pauza)))
    #time.sleep(1)
    context.browser.find_element_by_xpath('//*[@id="ui-accordiontab-'+ str(pokrice['id'])+'-content"]/div/app-pokrice-osiguranika/div/div/span[1]/input').send_keys(ID_POKRICA)

    time.sleep(1)
    #WebDriverWait(context.browser, 5).until(cond._element_if_visible((By.XPATH,'//*[@id="ui-accordiontab-'+ str(pokrice['id'])+'-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[8]/div/span')))
    span_element = context.browser.find_element_by_xpath('//*[@id="ui-accordiontab-'+ str(pokrice['id'])+'-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[8]/div/span')
    pokrice['rezervisaniIznos'] = float(span_element.text)
    print('Iznos na pokricu je: ' + str(pokrice['rezervisaniIznos']))
    #time.sleep(1)

@when("korisnik unosi (?P<STAVKA_CENA>.+), (?P<TERMIN>.+), (?P<DOKTOR>.+), (?P<ID_POKRICA>.+)")
def unosenje_podataka(context, STAVKA_CENA, TERMIN, DOKTOR, ID_POKRICA):
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/div/p-button[1]/button')))
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/div/p-button[1]/button').click()
    #time.sleep(0.5)
    WebDriverWait(context.browser, 5).until(cond.presence_of_element_located((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-autocomplete/span/input')))
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-autocomplete/span/input').send_keys(STAVKA_CENA)
    #time.sleep(1)
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.CSS_SELECTOR,'.ui-autocomplete-list-item')))
    context.browser.find_elements_by_css_selector('.ui-autocomplete-list-item')[0].click()
    #time.sleep(0.5)
    WebDriverWait(context.browser, 5).until(cond.presence_of_element_located((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-inputmask/input')))
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-inputmask/input').send_keys(TERMIN)
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[4]/div[2]/input').send_keys(DOKTOR)
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[5]/div[2]/p-autocomplete/span/input').send_keys(ID_POKRICA)
    #time.sleep(1)
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.CSS_SELECTOR,'.ui-autocomplete-list-item')))
    context.browser.find_elements_by_css_selector('.ui-autocomplete-list-item')[0].click()
    time.sleep(1)
    #WebDriverWait(context.browser, 5).until(cond.presence_of_element_located((By.PARTIAL_LINK_TEXT,"//*[contains(text(), 'Sačuvaj')]")))
    context.browser.find_elements_by_xpath("//*[contains(text(), 'Sačuvaj')]")[0].click()
    time.sleep(1.5)

@then("na pokriću rezervisan iznos treba da bude povecan za (?P<IZNOS>.+)")
def Da_li_je_dodat_novi_iznoos(context, IZNOS):
    span_element1 = context.browser.find_element_by_xpath('//*[@id="ui-accordiontab-'+ str(pokrice['id'])+'-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[8]/div/span')
    pokrice['id'] += 1
    novopokrice['NoviIznos'] = float(span_element1.text)
    IZNOS=float(IZNOS)
    print('Novi iznos na pokricu je: ' + str(novopokrice['NoviIznos']))
    assert (pokrice['rezervisaniIznos'])+(IZNOS) <= (novopokrice['NoviIznos'] and pokrice['rezervisaniIznos'])+(IZNOS)+0.02 >= (novopokrice['NoviIznos'])

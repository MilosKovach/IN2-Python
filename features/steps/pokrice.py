from behave import *

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
import time
from features.classes.document_page import Document_page
from features.classes.osiguranik_page import Osiguranik_page

use_step_matcher("re")

pokrice = {'rezervisaniIznos': 0, 'id': -1}
novopokrice = {'NoviIznos':0}

@given('postoji osiguranik sa ID brojem (?P<ID_OSIGURANIKA>.+)')
def ID_BR_OSIGURANIKA(context, ID_OSIGURANIKA):
    pokrice['id'] += 1
    context.browser.get('http://bg-ddordzo-01/dzo/#/home/osiguranici/'+ID_OSIGURANIKA)


@step("postoji dokument sa ID brojem (?P<ID_DOK>.+)")
def ID_BR_Dokumenta(context, ID_DOK):
    try:
        document1 = Osiguranik_page(context.browser)

    except NoSuchElementException:
        print('Ne postoji korisnik sa ovim podacima')

@step("postoji pokriće sa nazivom (?P<ID_POKRICA>.+)")
def ID_Pokrica(context, ID_POKRICA):
    document = Document_page(context.browser, pokrice['id'])
    document.unesi_naziv_pokrica_POKRICEPY(ID_POKRICA)
    pokrice['rezervisaniIznos'] = document.rezervisani_iznos()
    print('Stari iznos na pokricu je: ' + str(pokrice['rezervisaniIznos']))


@when("korisnik unosi (?P<STAVKA_CENA>.+), (?P<TERMIN>.+), (?P<DOKTOR>.+), (?P<ID_POKRICA>.+)")
def unosenje_podataka(context, STAVKA_CENA, TERMIN, DOKTOR, ID_POKRICA):
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/div/p-button[1]/button')))
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/div/p-button[1]/button').click()
    WebDriverWait(context.browser, 5).until(cond.presence_of_element_located((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-autocomplete/span/input')))
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-autocomplete/span/input').send_keys(STAVKA_CENA)
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.CSS_SELECTOR,'.ui-autocomplete-list-item')))
    context.browser.find_elements_by_css_selector('.ui-autocomplete-list-item')[0].click()

    WebDriverWait(context.browser, 5).until(cond.presence_of_element_located((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-inputmask/input')))
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-inputmask/input').send_keys(TERMIN)
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[4]/div[2]/input').send_keys(DOKTOR)
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[5]/div[2]/p-autocomplete/span/input').send_keys(ID_POKRICA)
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.CSS_SELECTOR,'.ui-autocomplete-list-item')))
    context.browser.find_elements_by_css_selector('.ui-autocomplete-list-item')[0].click()
    time.sleep(1)
    
    context.browser.find_elements_by_xpath("//*[contains(text(), 'Sačuvaj')]")[0].click()
    time.sleep(1.5)

@then("na pokriću rezervisan iznos treba da bude povecan za (?P<IZNOS>.+)")
def Da_li_je_dodat_novi_iznoos(context, IZNOS):
    span_element1 = context.browser.find_element_by_xpath('//*[@id="ui-accordiontab-'+ str(pokrice['id'])+'-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[8]/div/span')
    novopokrice['NoviIznos'] = float(span_element1.text)
    IZNOS=float(IZNOS)
    print('Novi iznos na pokricu je: ' + str(novopokrice['NoviIznos']))
    assert (pokrice['rezervisaniIznos']+(IZNOS) <= novopokrice['NoviIznos']) and (pokrice['rezervisaniIznos']+(IZNOS)+0.02 >= novopokrice['NoviIznos'])

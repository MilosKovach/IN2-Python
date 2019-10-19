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

@given("Postoji OS sa ID (?P<OS_ID>.+) i Dokument na tom OS sa ID (?P<DOK_ID>.+)")
def Osigurani_slucaj_sa_unetim_podacima (context, OS_ID, DOK_ID):
    context.browser.get('http://bg-ddordzo-01/dzo/#/home/osiguranici/osiguraniSlucaj/'+OS_ID+'/dokumenti/'+DOK_ID)

@step("postoji bar jedna stavka na tom dokumentu")
def Otvaranje_dokumenta(context):
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-table/div/div/table/tbody/tr/td[2]/span[2]').click()
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-table/div/div/table/tbody/tr/td[8]/div/button[1]').click()
    context.browser.find_element_by_xpath

@when("Korisnik doda novu dijagnozu (?P<DIJAGNOZA_OZNAKA>.+) na stavku")
def Dodavanje_dijagnoze_na_stavku(context, DIJAGNOZA_OZNAKA):
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-stavke-dokumenta-details/div[2]/app-sifarnik-table/div/p-button[1]/button').click()
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-stavke-dokumenta-details/div[2]/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]/p-autocomplete/span/input').send_keys(DIJAGNOZA_OZNAKA)
    time.sleep(0.5)
    context.browser.find_element_by_xpath('/html/body/div[2]/ul/li').click()
    time.sleep(0.5)
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-stavke-dokumenta-details/div[2]/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/textarea').send_keys('DR. Ljubo Lukovic')
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-stavke-dokumenta-details/div[2]/app-sifarnik-table/p-dialog[1]/div/div[3]/p-footer/button[1]').click()

@then('Na profilu osiguranika (?P<OSIGURANIK_ID>.+) treba da stoji upozorenje "Osiguranik je u drugom stanju..."')
def Provera_da_li_postoji_upozorenje_da_je_osiguranik_trudan(context, OSIGURANIK_ID):
    context.browser.get('http://bg-ddordzo-01/dzo/#/home/osiguranici/' + OSIGURANIK_ID)
    elementi = context.browser.find_elements_by_xpath("//*[contains(text(), 'Osiguranik je u drugom stanju')]")
    assert len(elementi) > 0

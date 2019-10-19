from behave import *
import selenium.webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
import context
import autopy
import pyautogui

use_step_matcher("re")


@given("Postoji PU sa Matičnim brojem (?P<PU_MB>.+)")
def Pruzaoc_usluga_PU_MB(context, PU_MB):
    try:
        context.browser.get('http://bg-ddordzo-01/dzo/#/home/pruzaociUsluga')
        context.browser.find_element_by_xpath(
            '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/p-button[2]/button').click()
        WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable(
            (By.XPATH, '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/span[1]/input')))
        context.browser.find_element_by_xpath(
            '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/div/span[1]/input').send_keys(
            PU_MB)
        time.sleep(1.33)
        # WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[2]')))
        context.browser.find_element_by_xpath(
            '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[2]').click()
        context.browser.find_element_by_xpath(
            '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzaoci-usluga/div/app-pruzalac-usluga-table/p-treetable/div/div/table/tbody/tr/td[8]/div/button[1]').click()
    except:
        print('Except u given')
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test/test1'+PU_MB+'.png')


# screenshoot

@when("Korisnik dodaje novo radno vreme za PU: (?P<RADNI_DAN>.+), (?P<TERMIN_OD>.+), (?P<TERMIN_DO>.+)")
def Dodavanje_novog_radnog_vrmena(context, RADNI_DAN, TERMIN_OD, TERMIN_DO):
    context.browser.find_element_by_xpath(
        '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/div[2]/p-tabmenu/div/ul/li[3]/a/span[2]').click()
    # Udji u radno vreme
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,
                                                                          '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/div/p-button/button')))
    context.browser.find_element_by_xpath(
        '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/div/p-button/button').click()
    # DODAJ,ovo gore
    time.sleep(1)

    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,
                                                                          '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]/p-dropdown/div/label')))
    context.browser.find_element_by_xpath(
        '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]/p-dropdown/div/label').click()

    context.browser.find_element_by_xpath('/html/body/div[2]/div[1]/input').send_keys(RADNI_DAN)
    # OVO GORE JE DROP DAN RADNOG VREMENA

    WebDriverWait(context.browser, 5).until(
        cond.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/ul/li/span')))
    context.browser.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li/span').click()

    # WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-inputmask/input')))
    time.sleep(1)
    context.browser.find_element_by_xpath(
        '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-inputmask/input').click()
    pyautogui.typewrite(TERMIN_OD)
    # WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-inputmask/input')))
    context.browser.find_element_by_xpath(
        '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-inputmask/input').click()
    pyautogui.typewrite(TERMIN_DO)
    # time.sleep(1)
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,
                                                                          '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[3]/p-footer/button[1]/span[2]')))
    context.browser.find_element_by_xpath(
        '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/app-radno-vreme/div/app-sifarnik-table/p-dialog[1]/div/div[3]/p-footer/button[1]/span[2]').click()
    time.sleep(1)
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test/test2.png')

@then("Na stranici sa detaljima PU (?P<PU_MB>.+) treba proveriti status (?P<STATUS>.+)")
def Provera_Da_li_Pruzaoc_usluga_radi_ili_ne(context, PU_MB, STATUS):
    context.browser.get('http://bg-ddordzo-01/dzo/#/home')
    time.sleep(1)
    context.browser.get('http://bg-ddordzo-01/dzo/#/home/pruzaociUsluga/' + str(PU_MB))

    WebDriverWait(context.browser, 5).until(cond.visibility_of_element_located((By.XPATH,
                                                                                '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/div[2]/p-tabmenu/div/ul/li[3]/a/span[2]')))
    try:
        span_element = context.browser.find_element_by_xpath(
            '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/div[1]/div[1]/div[12]/div')
        STATUS_RADNOG_VREMENA = (span_element.text.strip())
        assert STATUS_RADNOG_VREMENA == STATUS
    except AssertionError:
        span_element = context.browser.find_element_by_xpath(
            '/html/body/app-root/app-home/div/div[3]/div/div/app-pruzalac-usluga-details/div[1]/div[1]/div[14]/div')
        STATUS_RADNOG_VREMENA = span_element.text.strip()
        assert STATUS_RADNOG_VREMENA == STATUS
    time.sleep(2)
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test/test3'+PU_MB+'.png')
from behave import *
from selenium.common.exceptions import NoSuchElementException
import time
import pyautogui
use_step_matcher("re")


@given('korisnik se loguje na stranicu "https://http://bg-ddordzo-01/dzo"')
def otvaranje_aplikacije(context):
    context.browser.get('http://bg-ddordzo-01/dzo')

@when("korisnik informacije za logovanje (?P<KORISNIK>.+)")
def unosenje_podataka(context, KORISNIK):
    context.browser.find_element_by_id('username').click()
    pyautogui.typewrite(KORISNIK)


@step("korisnik unese sifru (?P<SIFRA>.+)")
def unosenje_sifre(context, SIFRA):
    context.browser.find_element_by_id('password').click()
    pyautogui.typewrite(SIFRA)

    context.browser.find_element_by_id('login').click()
    time.sleep(3)

@then("korisnik je ulogovan")
def ulogovan_korisnik(context):
    try:
        meni = context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul')
        assert meni is not None
    except NoSuchElementException:
        raise AssertionError('Username/sifra je pogresna')

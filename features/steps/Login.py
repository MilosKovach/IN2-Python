from behave import *

use_step_matcher("re")
from features.classes.Login import *
from features.classes.HomePage import *


@given('korisnik se loguje na stranicu "https://http://bg-ddordzo-01/dzo"')
def otvaranje_aplikacije(context):
    context.browser.get('http://bg-ddordzo-01/dzo')


@when("korisnik informacije za logovanje (?P<KORISNIK>.+)")
def unosenje_podataka(context, KORISNIK):
    login = Login(context.browser)
    login.username_send_text(KORISNIK)


@step("korisnik unese sifru (?P<SIFRA>.+)")
def unosenje_sifre(context, SIFRA):
    login = Login(context.browser)
    login.password_send_text(SIFRA)
    login.login_button_click()


@then("korisnik je ulogovan")
def ulogovan_korisnik(context):
    homepage = HomePage(context.browser)
    assert homepage.menu_list() is not None
    homepage.logout_button_click()


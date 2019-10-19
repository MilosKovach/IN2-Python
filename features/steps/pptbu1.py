from behave import *
import time
from features.classes.document_page import Document_page
use_step_matcher("re")
@given('Postoji Osigurani slučaj 5004 i na njemu dokument sa ID 993')
def OS_5004_ID_993(context):
    context.browser.get('http://bg-ddordzo-01/dzo/#/home/osiguranici/osiguraniSlucaj/5004/dokumenti/993')
    time.sleep(1)
@step('Dokument se odnosi na Osiguranika OKTAVIJAN GAGIĆ')
def Oktavijan_Gagic(context):
    document = Document_page(context.browser)
    assert document.ime() == 'OKTAVIJAN GAGIĆ'
@step('Za tog osiguranika postoji pokriće Dijagnostika CT,sa merom limita,Broj usluga,iskorisceno')
def Dijagnostika_CT_Broj_Usluga(context):
    document = Document_page(context.browser)
    document.nadji_pokrice('Dijagnostika CT')
    assert document.mera_limita() == 'Broj usluga'
@when('Korisnik doda novu stavku dokumenta: Color Doppler magistralnih arterija vrata, 1100, Petar Petrovic, Dijagnostika CT')
def Dodavanje_novih_stavki(context):
    document1 = Document_page(context.browser)
    document1.unesi_stavku('Color Doppler magistralnih arterija vrata', '1100', 'Petar Petrovic', 'Dijagnostika CT')
    document1.sacuvaj_novu_stavku()
@then('Na Pokrićima, za Dijagnostiku CT treba u koloni Iskorišćeno da stoji 1')
def Iskorisceno_jednako_1(context):
    document = Document_page(context.browser)
    document.provera_pokrica()
    time.sleep(1)
    assert document.iskorisceno_posle() == 1
@step('Dijagnostika CT treba da bude obojena crvenom bojom')
def Crveno_na_radost(context):
    document = Document_page(context.browser)
    assert document.boja_usluge() == 'rgba(255, 0, 0, 1)'

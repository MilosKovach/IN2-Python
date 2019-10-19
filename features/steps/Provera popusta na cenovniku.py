from behave import *
from selenium.webdriver.support import expected_conditions as cond
from features.classes.HomePage import *
from features.environment import *
import autopy

use_step_matcher("re")

@given("Postoji cenovnik sa ID (?P<CENOVNIK_ID>.+)")
def Otvaranje_stavke_cenovnici_sa_izabranim_ID(context, CENOVNIK_ID):
    context.browser.get('http://bg-ddordzo-01/dzo/#/home/cenovnici/'+CENOVNIK_ID)
    time.sleep(1)
    print('Given cenovnik')
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test01.png')

@when("Korisnik unese novu korekciju cenovnika:(?P<KOREKCIJA_NAZIV>.+),(?P<KOREKCIJA_TIP>.+),(?P<KOREKCIJA_OBIM>.+),(?P<KOREKCIJA_POPUST>.+)")
def Korisnik_unosi_potrebne_podatke(context, KOREKCIJA_NAZIV, KOREKCIJA_TIP, KOREKCIJA_OBIM, KOREKCIJA_POPUST):

    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test02'+KOREKCIJA_NAZIV+'.png')
    #WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'//*[@id="ui-accordiontab-1"]/span[2]')))
    time.sleep(1.5)


    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test01'+KOREKCIJA_NAZIV+'.png')

    context.browser.find_element_by_xpath('//*[@id="ui-accordiontab-0"]/span[2]').click()
    time.sleep(1)

    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test02'+KOREKCIJA_NAZIV+'.png')

    #WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'//*[@id="ui-accordiontab-0-content"]/div/app-korekcija-cenovnika/div/app-korekcija-cenovnika-table/div/p-button[1]/button')))
    context.browser.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-korekcija-cenovnika/div/app-korekcija-cenovnika-table/div/p-button[1]/button').click()
    time.sleep(1)

    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test03'+KOREKCIJA_NAZIV+'.png')


    #WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'//*[@id="ui-accordiontab-0-content"]/div/app-korekcija-cenovnika/div/app-korekcija-cenovnika-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]/input')))
    context.browser.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-korekcija-cenovnika/div/app-korekcija-cenovnika-table/p-dialog[1]/div/div[2]/div/div[1]/div[2]/input').send_keys(KOREKCIJA_NAZIV)
    #context.browser.find_element_by_xpath('/html/body/div[2]/div[1]/input').send_keys(KOREKCIJA_NAZIV)


    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test04'+KOREKCIJA_NAZIV+'.png')

    time.sleep(1)
    context.browser.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-korekcija-cenovnika/div/app-korekcija-cenovnika-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-dropdown/div/label').click()
    time.sleep(1)

    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test05' + KOREKCIJA_NAZIV + '.png')

    context.browser.find_element_by_xpath('/html/body/div[2]/div[1]/input').send_keys(KOREKCIJA_TIP)
    time.sleep(1)

    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test06' + KOREKCIJA_NAZIV + '.png')

    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/ul/li/span')))
    context.browser.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li/span').click()
    time.sleep(1)

    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test07' + KOREKCIJA_NAZIV + '.png')

    context.browser.find_element_by_xpath(' //*[@id="ui-accordiontab-0-content"]/div/app-korekcija-cenovnika/div/app-korekcija-cenovnika-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-dropdown/div/label').click()
    time.sleep(1)

    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test08' + KOREKCIJA_NAZIV + '.png')

    context.browser.find_element_by_xpath('/html/body/div[2]/div[1]/input').send_keys(KOREKCIJA_OBIM)
    time.sleep(1)
    #WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'/html/body/div[2]/div[2]/ul/li/span')))

    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test08' + KOREKCIJA_NAZIV + '.png')

    context.browser.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li/span').click()
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'//*[@id="ui-accordiontab-0-content"]/div/app-korekcija-cenovnika/div/app-korekcija-cenovnika-table/p-dialog[1]/div/div[2]/div/div[4]/div[2]/input')))
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test09' + KOREKCIJA_NAZIV + '.png')

    context.browser.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-korekcija-cenovnika/div/app-korekcija-cenovnika-table/p-dialog[1]/div/div[2]/div/div[4]/div[2]/input').send_keys(KOREKCIJA_POPUST )

    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test10' + KOREKCIJA_NAZIV + '.png')

    context.browser.find_element_by_xpath('//*[@id="ui-accordiontab-0-content"]/div/app-korekcija-cenovnika/div/app-korekcija-cenovnika-table/p-dialog[1]/div/div[3]/p-footer/button[1]').click()


@step("Korisnik osvezi stavke cenovnika")
def Osvezavanje_stranice(context):
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test11.png')

    time.sleep(1)
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-details/div/div[2]/app-usluga-pu/div/div/p-button[1]/button').click()
    time.sleep(1)

    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test12.png')

@then("Na stavci (?P<STAVKA_NAZIVA>.+) cena sa popustom treba da bude pravilno umanjena za (?P<KOREKCIJA_POPUST>.+)procenata")
def Provera_da_li_je_popust_pravilno_izracunat(context, STAVKA_NAZIVA, KOREKCIJA_POPUST):
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-details/div/div[2]/app-usluga-pu/div/div/span[1]/p-autocomplete/span/input').send_keys(STAVKA_NAZIVA)
    WebDriverWait(context.browser, 5).until(cond.element_to_be_clickable((By.XPATH,'/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-details/div/div[2]/app-usluga-pu/div/div/span[1]/p-autocomplete/span/div/ul/li')))
    context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-details/div/div[2]/app-usluga-pu/div/div/span[1]/p-autocomplete/span/div/ul/li').click()
    time.sleep(2)
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test13.png')

    span_element = context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-details/div/div[2]/app-usluga-pu/div/app-usluga-pu-table/p-table/div/div/table/tbody/tr[1]/td[5]/span[2]')
    span_element_popust = context.browser.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-cenovnik-details/div/div[2]/app-usluga-pu/div/app-usluga-pu-table/p-table/div/div/table/tbody/tr[1]/td[6]/span[2]')
    #novopokrice['NoviIznos'] = float(span_element1.text)

    Stara_cena= float(span_element.text.replace(",", ""))
    Nova_cena=float(span_element_popust.text.replace(",", ""))
    assert(Stara_cena*((100-(float(KOREKCIJA_POPUST)))/100)== Nova_cena)
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('C:/Users/milosk/Desktop/test provera popusta/test14.png')


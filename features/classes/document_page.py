from features.classes.Login import *
import time


class Document_page:
    IME_OSIGURANIKA_BY_XPATH = (
        '/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/div/div[1]/div[10]')
    NAZIV_POKRICA_BY_XPATH = ('//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/div/span[1]/input')
    MERA_LIMITA_BY_XPATH = (
        '//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[6]/div/span')
    ISKORISCENO_PRE_BY_XPATH = (
        '//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[11]/div')
    DODAJ_NOVU_STAVKU_UPUTA_BY_XPATH = (
        '/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/div/p-button[1]/button')

    UNOS_STAVKE_CENOVNIKA_BY_XPATH = (
        '/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[2]/div[2]/p-autocomplete/span/input')

    PADAJUCI_MENI_UNOSA_STAVKI_BY_XPATH = ('/html/body/div[2]/ul')
    UNOS_TERMINA_BY_XPATH = (
        '/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[3]/div[2]/p-inputmask/input')

    IME_LEKARA_BY_XPATH = (
        '/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[4]/div[2]/input')

    UNOS_STAVKE_POKRICA_BY_XPATH = (
        '/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[2]/div/div[5]/div[2]/p-autocomplete/span/input')

    PADAJUCI_MENI_UNOS_STAVKE_POKRICA_BY_XPATH = ('/html/body/div[2]/ul')
    SACUVAJ_NOVU_STAVKU_UPUTA_BY_XPATH = (
        '/html/body/app-root/app-home/div/div[3]/div/div/app-dokument-details/app-stavke-uputa/div/app-stavke-uputa-table/p-dialog[1]/div/div[3]/p-footer/button[1]')
    ISKORISCENO_POSLE_BY_XPATH = (
        '//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[11]/div/span')

    BOJA_USLUGE_BY_XPATH = (
        '//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[1]/div')

    '''POKRICE.PY                       POKRICE.PY                          POKRICE.PY                                         POKRICE.PY'''

    POKRICA_OSIGURANIKA_BY_XPATH = ('//*[@id="ui-accordiontab-0"]/span[2]')  # POKRICA OSIGURANIKA
    NAZIV_POKRICA_UNOS_BY_XPATH = (
        '//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/div/span[1]/input')
    REZERVISANI_IZNOS_BY_XPATH = (
        '//*[@id="ui-accordiontab-0-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[8]/div/span')

    def __init__(self, browser):
        self.browser = browser
        self.pokrice_id = 0
        self._ime = browser.find_element(By.XPATH, self.IME_OSIGURANIKA_BY_XPATH)
        self._pokrice_osiguranja = browser.find_element(By.XPATH, self.POKRICA_OSIGURANIKA_BY_XPATH)
        self._naziv_pokrica = browser.find_element(By.XPATH, self.NAZIV_POKRICA_BY_XPATH)
        self._dodaj_novu_stavku_uputa = browser.find_element(By.XPATH, self.DODAJ_NOVU_STAVKU_UPUTA_BY_XPATH)
        self._iskorisceno_pre = browser.find_element(By.XPATH, self.ISKORISCENO_PRE_BY_XPATH)
        self._boja_usluge = browser.find_element(By.XPATH, self.BOJA_USLUGE_BY_XPATH)

    def __init__(self, browser, pokrice_id):
        self.browser = browser
        self.pokrice_id = pokrice_id
        self._ime = browser.find_element(By.XPATH, self.IME_OSIGURANIKA_BY_XPATH)
        self._pokrica_osiguranika = browser.find_element(By.XPATH,
                                                         ('//*[@id="ui-accordiontab-' + str(pokrice_id) + '"]/span[2]'))
        self._naziv_pokrica = browser.find_element(By.XPATH, ('//*[@id="ui-accordiontab-' + str(
            pokrice_id) + '-content"]/div/app-pokrice-osiguranika/div/div/span[1]/input'))
        self._dodaj_novu_stavku_uputa = browser.find_element(By.XPATH, self.DODAJ_NOVU_STAVKU_UPUTA_BY_XPATH)
        self._iskorisceno_pre = browser.find_element(By.XPATH, '//*[@id="ui-accordiontab-' + str(
            pokrice_id) + '-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[11]/div')

    def ime(self):
        return self._ime.text

    def mera_limita(self):
        return self._mera_limita.text

    def iskorisceno_pre(self):
        return self._iskorisceno_pre.text

    def iskorisceno_posle(self):
        self._iskorisceno_posle = self.browser.find_element(By.XPATH, self.ISKORISCENO_POSLE_BY_XPATH)

        return float(self._iskorisceno_posle.text)

    def boja_usluge(self):
        return self._boja_usluge.value_of_css_property('color')

    def nadji_pokrice(self, naziv_pokrica):
        self.browser.find_element_by_xpath('//*[@id="ui-accordiontab-' + str(self.pokrice_id) + '"]/span[2]').click()
        self.browser.find_element_by_xpath(
            '//*[@id="ui-accordiontab-' + str(
                self.pokrice_id) + '-content"]/div/app-pokrice-osiguranika/div/div/span[1]/input').send_keys(
            naziv_pokrica)
        time.sleep(1)

        self._mera_limita = self.browser.find_element_by_xpath(
            '//*[@id="ui-accordiontab-' + str(
                self.pokrice_id) + '-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[6]/div/span')

    def unesi_stavku(self, usluga, termin, doktor, pokrice):
        self._dodaj_novu_stavku_uputa.click()

        self._unos_stavke_cenovnika = self.browser.find_element(By.XPATH, self.UNOS_STAVKE_CENOVNIKA_BY_XPATH)
        self._unos_stavke_cenovnika.send_keys(usluga)
        self._padajuci_meni_unosa_stavki = self.browser.find_element(By.XPATH, self.PADAJUCI_MENI_UNOSA_STAVKI_BY_XPATH)
        self._padajuci_meni_unosa_stavki.click()
        self._unos_termina = self.browser.find_element(By.XPATH, self.UNOS_TERMINA_BY_XPATH)
        self._unos_termina.send_keys(termin)

        self._ime_lekara = self.browser.find_element(By.XPATH, self.IME_LEKARA_BY_XPATH)
        self._ime_lekara.send_keys(doktor)

        self._unos_stavke_pokrica = self.browser.find_element(By.XPATH, self.UNOS_STAVKE_POKRICA_BY_XPATH)
        self._unos_stavke_pokrica.send_keys(pokrice)
        self._padajuci_meni_pokrica = self.browser.find_element(By.XPATH,
                                                                self.PADAJUCI_MENI_UNOS_STAVKE_POKRICA_BY_XPATH)
        self._padajuci_meni_pokrica.click()

    def sacuvaj_novu_stavku(self):
        self._sacuvaj_novu_stavku_uputa = self.browser.find_element(By.XPATH, self.SACUVAJ_NOVU_STAVKU_UPUTA_BY_XPATH)
        self._sacuvaj_novu_stavku_uputa.click()
        time.sleep(1)

    def provera_pokrica(self):
        self._mera_limita = self.browser.find_element(By.XPATH, self.MERA_LIMITA_BY_XPATH)
        self._iskorisceno_posle = self.browser.find_element(By.XPATH, self.ISKORISCENO_POSLE_BY_XPATH)

    def unesi_naziv_pokrica_POKRICEPY(self, Id_pokrica):
        self._pokrica_osiguranika = self.browser.find_element(By.XPATH, '//*[@id="ui-accordiontab-' + str(
            self.pokrice_id) + '"]/span[2]').click()
        self._naziv_pokrica_unos = self.browser.find_element(By.XPATH, '//*[@id="ui-accordiontab-' + str(
            self.pokrice_id) + '-content"]/div/app-pokrice-osiguranika/div/div/span[1]/input')
        self._naziv_pokrica_unos.send_keys(Id_pokrica)

    def rezervisani_iznos(self):
        time.sleep(1)
        self._rezervisani_iznos_POKRICEPY = self.browser.find_element(By.XPATH,                                                                   '//*[@id="ui-accordiontab-' + str(
                                                                          self.pokrice_id) + '-content"]/div/app-pokrice-osiguranika/div/app-pokrice-osiguranika-table/p-table/div/div/table/tbody/tr/td[8]/div/span')
        return float(self._rezervisani_iznos_POKRICEPY.text)

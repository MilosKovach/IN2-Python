from features.classes.Login import *
import time

class Osiguranik_page:
    OSIGURANI_SLUCAJEVI_BY_XPATH = ('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/div[2]/p-tabmenu/div/ul/li[2]/a/span[2]')
    OBELEZI_OSIGURANI_SLUCAJ_BY_XPATH = ('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-table/div/div/table/tbody/tr[1]/td[1]')  # KLIK NA POLISU OSIGURANJA,OBELEZI
    DETALJNIJE_OBELEZI___BY_XPATH = ('/html/body/app-root/app-home/div/div[3]/div/div/app-osiguranik-details/app-osigurani-slucaj/div/app-osigurani-slucaj-table/p-table/div/div/table/tbody/tr/td[6]/div/button[1]')  # DETALJNIJE
    OBELEZI_STAVKU_UPUTA_UNUTAR_OSIG_SLUCAJA_BY_XPATH = ('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/p-table/div/div/table/tbody/tr/td[2]/span[2]/div/span')  # ID DOKUMENTA(1080)ID DOK
    DETALJNIJE_STAVKA_UPUTA_BY_XPATH = ('/html/body/app-root/app-home/div/div[3]/div/div/app-osigurani-slucaj-details/div[2]/app-dokument/div/app-dokument-table/p-table/div/div/table/tbody/tr/td[13]/div/button[1]')  # Detaljnije opet


    def __init__(self, browser):
        self.browser = browser
        self._osigurani_slucajevi = self.browser.find_element(By.XPATH, self.OSIGURANI_SLUCAJEVI_BY_XPATH).click()
        time.sleep(1)
        self._obelezi_osigurani_slucaj = self.browser.find_element(By.XPATH, self.OBELEZI_OSIGURANI_SLUCAJ_BY_XPATH).click()
        self._detaljnije_obeleziosiguranislucaj = self.browser.find_element(By.XPATH, self.DETALJNIJE_OBELEZI___BY_XPATH).click()
        self._obelezi_stavku_uputa = self.browser.find_element(By.XPATH, self.OBELEZI_STAVKU_UPUTA_UNUTAR_OSIG_SLUCAJA_BY_XPATH).click()
        self._detaljnije_stavka_uputa = self.browser.find_element(By.XPATH, self.DETALJNIJE_STAVKA_UPUTA_BY_XPATH).click()

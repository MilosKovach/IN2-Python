from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from features.classes.Logger import *

logger = set_logger()

'''Provera da li postoji neki od elemenata stranice koji se pojavljuju samo ako je korisnik pravilno ulogovan'''


class HomePage:
    LOGOUT_BUTTON_BY_CSS_SELECTOR = '#topbar-icons > a:nth-child(3) > span.topbar-icon.fa.fa-sign-out'
    MENU_LIST_XPATH = '/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul'

    def __init__(self, browser):
        try:
            self.__logout = browser.find_element(By.CSS_SELECTOR, self.LOGOUT_BUTTON_BY_CSS_SELECTOR)
            self._menu_list = browser.find_element(By.XPATH, self.MENU_LIST_XPATH)

        except(NoSuchElementException, TimeoutException):
            self._menu_list = None
            self.__logout = None
            logger.debug("Some of the elements are not found on user account main page!")

    def menu_list(self):
        logger.debug('Poruka Debug')
        logger.error('Poruka Debug')
        logger.info('Poruka Debug')
        return self._menu_list

    def get_logout(self):
        return self.__logout

    def logout_button_click(self):
        self.get_logout().click()

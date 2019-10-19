from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

'''Klasa koja se primenju za login stranice, opsta klasa, pocetnicki primer LOGIN'''


class Login:
    USERNAME_INPUT_FIELD_BY_ID = "username"
    PASSWORD_TEXT_INPUT_FIELD_BY_ID = "password"
    LOGIN_BUTTON_BY_ID = "login"

    def __init__(self, browser):
        self.browser = browser
        try:
            self.__username = browser.find_element(By.ID, self.USERNAME_INPUT_FIELD_BY_ID)
            self.__password = browser.find_element(By.ID, self.PASSWORD_TEXT_INPUT_FIELD_BY_ID)
            self.__login = browser.find_element(By.ID, self.LOGIN_BUTTON_BY_ID)

        except(NoSuchElementException, TimeoutException):
            print("Some of the elements are not found on user account main page!")

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_login(self):
        return self.__login

    def username_send_text(self, username):
        self.get_username().clear()
        self.get_username().send_keys(username)

    def password_send_text(self, password):
        self.get_password().clear()
        self.get_password().send_keys(password)

    def login_button_click(self):
        self.get_login().click()

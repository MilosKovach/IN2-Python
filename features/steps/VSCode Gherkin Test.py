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


@given ('Browser je otvoren')
def Browser_je_otvoren(context):
    context.browser.get('google.com ')

@when ('Kada u pretrazi otkucamo Beograd')
def Pretraga_Beograd(context):
    context.browser.find_element_by_xpath('//*[@id="q"]').send_keys("Beograd Slike")

@then ('Otvara se stranica Google-a sa slikama Beograda')
def Slike_Beograda(context):
    assert element_
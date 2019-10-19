
import os
import webbrowser
import pyautogui
import time
import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException



driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://bg-ddordzo-01/dzo/#/session')

time.sleep(1)

id='username'
btn=driver.find_element_by_id(id)
btn.click()


pyautogui.typewrite ('dcirovic')
pyautogui.press('enter')

csss='password'
btnn=driver.find_element_by_id(csss)
btnn.click()
pyautogui.typewrite('1234asdf')

lgn='login'
btnn1=driver.find_element_by_id(lgn)
btnn1.click()

time.sleep(1)
try:
    padajuca_lista = driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul')
    sifrarnici=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[7]/a/span')
    sifrarnici.click()

except NoSuchElementException:
    time.sleep(1)
    os.system("notepad.exe Greska404.txt")
time.sleep(1)
mesta=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[2]/p-scrollpanel/div/div[1]/div/div/app-menu/div/ul/ul/li[7]/ul/ul/li[2]/a/span')
mesta.click()

time.sleep(1)
dodaj_novo_mesto=driver.find_element_by_css_selector('body > app-root > app-home > div > div.main > div > div > app-mesto-list > div > app-sifarnik-table > div > p-button.ng-star-inserted > button > span.ui-button-text.ui-clickable')
dodaj_novo_mesto.click()

time.sleep(0.5)

ime_mesta=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-mesto-list/div/app-sifarnik-table/p-dialog[1]/div/div[2]/div/div/div[2]/input')
ime_mesta.click()

pyautogui.typewrite ('Rugi Krtur')
sacuvaj=driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-mesto-list/div/app-sifarnik-table/p-dialog[1]/div/div[3]/p-footer/button[1]/span[2]')
sacuvaj.click()
time.sleep(1)

try:
    postoji_mesto = driver.find_element_by_xpath('/html/body/app-root/app-home/div/div[3]/div/div/app-mesto-list/div/app-sifarnik-table/p-dialog[1]/div/div[3]/p-footer/button[1]/span[2]')
    os.system('notepad.exe Greska409.txt')
    time.sleep(1)


except:
    sacuvano = driver.find_element_by_xpath('/html/body/app-root/p-growl/div/div/div/div[2]/span')
    # uspesno dodato
    os.system('notepad.exe Greska410.txt')
    time.sleep(1)



else:
    NoSuchElementException
    time.sleep(1)


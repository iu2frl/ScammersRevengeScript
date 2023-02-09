from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
import string
import ccgenerator
from random import Random

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

url = "https://puoesserecompletatorapidamenteefacilmente.friulhosting.it/"
browser = webdriver.Chrome()

while (True):
    browser.get(url)
    browser.find_element(By.ID, "loginpage-logincontroller-login-user").send_keys(str(random.randint(11111111, 99999999)))
    browser.find_element(By.ID, "loginpage-logincontroller-login-pin").send_keys(str(random.randint(11111, 99999)))
    browser.find_element(By.ID, "enter1Login").click()
    browser.find_element(By.NAME, "nome").send_keys(get_random_string(8))
    browser.find_element(By.NAME, "cognome").send_keys(get_random_string(8))
    browser.find_element(By.NAME, "cellulare").send_keys(str(random.randint(3333333333, 3500000000)))
    browser.find_element(By.ID, "enter1Login").click()
    generator = Random()
    generator.seed()        # Seed from current time
    ccnum: str = ccgenerator.credit_card_number(generator, ccgenerator.mastercardPrefixList, 16)
    for b in ccnum:
      browser.find_element(By.NAME, "cc").send_keys(b)
      time.sleep(0.001)
    browser.find_element(By.NAME, "exp").send_keys(str(random.randint(1, 12)))
    time.sleep(0.01)
    browser.find_element(By.NAME, "exp").send_keys(str(random.randint(23, 30)))
    browser.find_element(By.NAME, "cvv").send_keys(str(random.randint(111, 999)))
    browser.find_element(By.ID, "enter1Login").click()
    time.sleep(1)
    
browser.quit()

import pytest_html_reporter
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
options.add_experimental_option("detach", True)

def test_LogIn():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('https://www.instagram.com/')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "input._aa4b._add6._ac4d")))\
        .send_keys('micha3lol')

    wait.until(EC.element_to_be_clickable((By.NAME,
                                      "password")))\
        .send_keys('m2692004+')

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      "button._acan._acap._acas")))\
        .click()
    
    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._acan._acao._acas")))\
        .click()

    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._a9--._a9_1")))\
        .click()

    driver.save_screenshot("resultados/login_successfull.png")


def test_LogInUnssucessful():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('https://www.instagram.com/')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                       "input._aa4b._add6._ac4d")))\
        .send_keys('micha3lol')

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.NAME,
                                      "password")))\
        .send_keys('m2692004')

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      "button._acan._acap._acas")))\
        .click()

    time.sleep(3)
    driver.save_screenshot("resultados/login_fail.png")


def test_AboutPage():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('https://www.instagram.com/')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "input._aa4b._add6._ac4d")))\
        .send_keys('micha3lol')

    wait.until(EC.element_to_be_clickable((By.NAME,
                                      "password")))\
        .send_keys('m2692004+')

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      "button._acan._acap._acas")))\
        .click()

    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._acan._acao._acas")))\
        .click()

    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._a9--._a9_1")))\
        .click()

    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "a._ab8g")))\
        .click()
    driver.save_screenshot("resultados/AboutPage.png")

def test_refreshpage():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('https://www.instagram.com/')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "input._aa4b._add6._ac4d")))\
        .send_keys('micha3lol')

    wait.until(EC.element_to_be_clickable((By.NAME,
                                      "password")))\
        .send_keys('m2692004+')

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      "button._acan._acap._acas")))\
        .click()

    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._acan._acao._acas")))\
        .click()

    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._a9--._a9_1")))\
        .click()
    
    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "a.x1i10hfl xjbqb8w x6umtig x1b1mbwd xaqea5y xav7gou x9f619 x1ypdohk xt0psk2 xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1a2a7pz _a6hd".replace(' ','.'))))\
        .click()
    driver.save_screenshot("resultados/pagina_refrescada.png")

def test_report():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('https://www.instagram.com/')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "input._aa4b._add6._ac4d")))\
        .send_keys('micha3lol')

    wait.until(EC.element_to_be_clickable((By.NAME,
                                      "password")))\
        .send_keys('m2692004+')

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      "button._acan._acap._acas")))\
        .click()

    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._acan._acao._acas")))\
        .click()

    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._a9--._a9_1")))\
        .click()
    
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._abl-")))\
        .click()
    
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._a9--._a9-_")))\
        .click()
    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._abn2")))\
        .click()

    time.sleep(4)
    driver.save_screenshot("resultados/spamreport.png")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._acan._acap._acas")))\
        .click()

def test_search():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get('https://www.instagram.com/')

    wait = WebDriverWait(driver, 10)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "input._aa4b._add6._ac4d")))\
        .send_keys('micha3lol')

    wait.until(EC.element_to_be_clickable((By.NAME,
                                      "password")))\
        .send_keys('m2692004+')

    time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                      "button._acan._acap._acas")))\
        .click()

    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._acan._acao._acas")))\
        .click()

    time.sleep(4)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "button._a9--._a9_1")))\
        .click()

    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "div._aacl._aacp._aacu._aacx._aada".replace(' ', '.'))))\
        .click()
    time.sleep(3)
    driver.save_screenshot("resultados/recentsearch.png")
    
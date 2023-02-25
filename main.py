import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

global URL, username, password, interval

URL = 'https://nys.x5.international.travian.com/'
username = 'Lord Voldemort'
password = '**********'
listas_a_atracar=[1,2,3,4]
interval = 600
village_name = "01"


def setup():
    driver.get(URL)
    driver.maximize_window()
    time.sleep(3)
    aceptar_cookies = driver.find_element(By.ID, 'cmpwelcomebtnyes')
    aceptar_cookies.click()
    username_field = driver.find_element(By.XPATH, './/input[contains(@name,"name")]')
    password_field = driver.find_element(By.XPATH, './/input[contains(@name,"password")]')
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button = driver.find_element(By.XPATH, './/button[contains(@type,"submit")]')
    login_button.click()
    time.sleep(3)


def atracar():
    centro= driver.find_element(By.XPATH,'//a[contains(@class,"village buildingView")]')
    centro.click()
    time.sleep(2)
    listas = driver.find_element(By.XPATH, './/span[contains(text(),"listas")]')
    listas.click()
    time.sleep(2)
    start = driver.find_elements(By.XPATH, './/button[contains(@value,"Start")]')
    for i in listas_a_atracar:
        start[i-1].click()
        time.sleep(2)

if __name__ == '__main__':
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    setup()

    while True:
        try:
            atracar()
            z=random.randint(interval - int(interval / 6), interval + int(interval / 6))
            print("now will wait: " + str(z))
            time.sleep(z)

        except:
            pass

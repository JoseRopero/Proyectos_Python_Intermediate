import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(os.environ['WEB'])
time.sleep(5)

# INICIO DE SESIÓN
driver.find_element(By.CLASS_NAME, 'nav__button-secondary').click()
time.sleep(5)
driver.find_element(By.ID, 'username').send_keys(os.environ['EMAIL'])
driver.find_element(By.ID, 'password').send_keys(os.environ['PASSWORD'])
driver.find_element(By.CLASS_NAME, 'btn__primary--large').click()
time.sleep(5)

driver.find_element(By.CLASS_NAME, 'jobs-save-button').click()


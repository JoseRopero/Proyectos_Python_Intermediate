import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

load_dotenv()

# Vamos a usar BeautifulSoup para sacar de la web los listados
# Lista con las direcciones de inmuebles
# Lista con los precios
# Lista con los enlaces

URL = 'https://appbrewery.github.io/Zillow-Clone/'

response = requests.get(URL)
web_zillow = response.text

soup = BeautifulSoup(web_zillow, 'html.parser')
print(soup.prettify())

# ------------------ Listado de las direcciones -------------------------------------------
address = soup.select('li address')

name_address = []
for name in address:
    name_text = name.getText().strip()
    if '|' in name_text:
        name_text_final = name_text.replace('|', ',')
        name_address.append(name_text_final)
    else:
        name_address.append(name_text)

print(f'Hay {len(name_address)} direcciones en total')

# ------------------ Listado con los enlaces ---------------------------------------------
links = soup.select('li .StyledPropertyCardDataWrapper a')

name_links = []
for name in links:
    name_links.append(name.get('href'))

print(f'Hay {len(name_links)} links en total')

# ------------------ Listado con los precios ------------------------------------------------
prices = soup.select('li .PropertyCardWrapper span')

name_prices = []
for price in prices:
    price_final = price.getText()
    if '+' in price_final:
        price_final_1 = price_final.split('+')[0]
        name_prices.append(price_final_1)
    else:
        price_final_1 = price_final.split('/')[0]
        name_prices.append(price_final_1)

print(f'Hay {len(name_prices)} prices en total')

# Ahora usamos Selenium para abrir el formulario y rellenarlo con todas las direcciones.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

for i in range(len(name_address)):
    driver.get(os.environ['FORMULARIO'])
    time.sleep(3)

    direccion = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div['
                                              '1]/div/div[1]/input')

    precio = driver.find_element(By.XPATH,
                                 '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div['
                                 '1]/input')

    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div['
                                         '1]/input')

    buttom = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    direccion.send_keys(name_address[i])
    precio.send_keys(name_prices[i])
    link.send_keys(name_links[i])
    time.sleep(2)
    buttom.click()
    time.sleep(2)

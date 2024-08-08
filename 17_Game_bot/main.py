from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re  # Para trabajar con expresiones regulares

TIME_OUT = time.time() + 5  # 5 segundos después del tiempo actual
FIVE_MIN = time.time() + 60 * 5

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Localizamos la galleta para realizar los clics
cookies = driver.find_element(By.ID, 'cookie')

# Guardamos los ids de las mejoras en un listado
linea_id = driver.find_elements(By.CSS_SELECTOR, '#store div')
list_id = []
for items in linea_id:
    name_id = items.get_attribute('id')
    list_id.append(name_id)

while True:
    cookies.click() # Realizamos el clic en la galleta

    # Verificamos si han pasado 5 segundos desde la última mejora
    if time.time() > TIME_OUT:
        # Buscamos las líneas que contienen los precios y los nombres
        shop = driver.find_elements(By.CSS_SELECTOR, '#store b')

        # Ahora iteramos para separar el precio del nombre y convertirlo en entero
        item_prices = []
        for store in shop:
            linea = store.text
            if '-' in linea:  # Verifica que la línea contiene un guion
                extraer_numero = linea.split('-')[1].strip()  # Extrae el texto después del guion y elimina espacios
                numero = int(re.sub(r'\D', '', extraer_numero))
                item_prices.append(numero)

        # Creamos un diccionario con las mejoras
        cookie_upgrades = {}
        for i in range(len(item_prices)):
            # Llenamos el diccionario con el precio de la mejora como clave y el ID como valor
            cookie_upgrades[item_prices[i]] = list_id[i]

        # Obtenemos la cantidad actual de cookies
        money = driver.find_element(By.ID, 'money').text
        if ',' in money:
            money = money.replace(',', '')
        money_number = int(money)

        # Creamos un diccionario con las mejoras que puede permitirse
        affordable_upgrades = {}
        for cost, id_number in cookie_upgrades.items():
            if money_number > cost:  # Verificamos si tiene bastantes cookies para la mejora
                affordable_upgrades[cost] = id_number  # Añadimos la mejora

        # Si hay mejoras
        if affordable_upgrades:
            # Buscamos la mejora más cara que puede permitirse
            highest_price_affordable_upgrade = max(affordable_upgrades)
            print(highest_price_affordable_upgrade)
            # Obtenemos el ID de la mejora
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            # Hacemos clic en la mejora que buscamos por el ID
            driver.find_element(by=By.ID, value=to_purchase_id).click()
        else:
            print('No hay mejoras')

        timeout = time.time() + 5
    if time.time() > FIVE_MIN:
        # Salimos del bucle e imprimimos las cookies por segundo
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break

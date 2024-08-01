from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Cargamos las variables de entorno
load_dotenv()

# Obtenemos el precio de la web
URL = 'https://appbrewery.github.io/instant_pot/'
URL_LIVE = ('https://www.amazon.es/edihome-Freidora-Unidades-Desechable-Accesorios/dp/B0D3VCV459?ref_'
            '=Oct_d_obs_d_2165363031_4&pd_rd_w=oO5ga&content-id=amzn1.sym.89a799ca-b7d7-4e0d-8ede-6c5bb6ace584'
            '&pf_rd_p=89a799ca-b7d7-4e0d-8ede-6c5bb6ace584&pf_rd_r=FXQ6SVS2AV8DGYK2MX3Z&pd_rd_wg=C6sf6&pd_rd_r'
            '=dfadd852-b66d-4bd8-ba1c-516183f8cada&pd_rd_i=B0D3VCV459&th=1')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
}

response = requests.get(URL, headers=headers)
web_amazon = response.text

soup = BeautifulSoup(web_amazon, 'html.parser')
print(soup.prettify())

precio = soup.find(class_='aok-offscreen').getText()
print(precio)
remove_dollar = precio.split('$')[1]
precio_float = float(remove_dollar)

print(precio_float)

# Nos enviamos el correo
titulo = soup.find(id='productTitle').getText().strip()
if precio_float < 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=os.environ['EMAIL'], password=os.environ['PASSWORD'])
        connection.sendmail(from_addr=os.environ['EMAIL'],
                            to_addrs=os.environ['EMAIL2'],
                            msg=f"El precio de {titulo} ha bajado de 100 dolares. Siga este enlace\n "
                                f"https://appbrewery.github.io/instant_pot/".encode('utf-8'))


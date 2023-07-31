import requests
from twilio.rest import Client
import config

# Aviso por sms cuando las acciones incrementan o decrementan en más de un 3% y envio de 3 noticias sobre la empresa.

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


END_POINT_ALPHA = "https://www.alphavantage.co/query"
KEY_ALPHA = config.KEY_ALPHA
END_POINT_NEWS = "https://newsapi.org/v2/everything"
KEY_NEWS = config.KEY_NEWS
ACCOUNT_SID = config.ACCOUNT_SID
AUTH_TOKEN = config.AUTH_TOKEN


parameters_alpha = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": KEY_ALPHA
}

parameters_news = {
    "apiKey": KEY_NEWS,
    "q": COMPANY_NAME,
}

# STEP 1: Use https://www.alphavantage.co

response = requests.get(END_POINT_ALPHA, params=parameters_alpha)
response.raise_for_status()
datos = response.json()

datos_days = datos['Time Series (Daily)']
# Hacemos una lista solo con las claves que son las fechas para poder escoger las dos últimas
fechas = list(datos_days.keys())
ultimo_dia = datos_days[fechas[0]]
penultimo_dia = datos_days[fechas[1]]
# Una vez que tenemos los dos últimos dias, nos hacemos con los datos de cierre.
cierre_ultimo_dia = float(ultimo_dia['4. close'])
cierre_penultimo = float(penultimo_dia['4. close'])
print(f"{cierre_ultimo_dia}\n{cierre_penultimo}")

# Cálculo del porcentaje de incremento o decremento.
diferencia = (float(cierre_ultimo_dia) - float(cierre_penultimo))
emoji = ""
if diferencia > 0:  # Si la diferencia es positiva es que es un incremento. Creamos el emoji para el sms
    emoji = "📈"
else:
    emoji = "📉"
porcentaje = round((diferencia / float(cierre_ultimo_dia)) * 100)  # Calculamos el porcentaje.
print(porcentaje)

# Cuando el porcentaje es mayor que 4 imprimimos 3 noticias sobre Tesla
# Use https://newsapi.org
if abs(porcentaje) > 3:
    response_news = requests.get(END_POINT_NEWS, parameters_news)
    response_news.raise_for_status()
    datos_3news = response_news.json()['articles'][:3]  # Nos quedamos con las 3 primeras noticias
    # Creamos una lista con el título y la descripción de cada noticia
    # "Headline: título.\n Brief: descripción"  -> este sería el formato
    mensajes = [f"{STOCK}: {emoji}{porcentaje}%\nHeadline: {articulo['title']}. \nBrief: {articulo['description']}" for articulo in datos_3news]
    print(mensajes)
# STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    for mensaje in mensajes:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)  # Realizamos la conexión para enviar el sms
        message = client.messages \
            .create(
                    body=mensaje,
                    from_='+17622525735',
                    to=config.TELEPHONE
            )
        print(message.status)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

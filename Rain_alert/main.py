import requests
from twilio.rest import Client  # Para enviar sms

# Probamos una API con API Key para autentificarnos.
# El ejercicio consiste en una app que nos avise por sms si va a llover en las próximas 12 horas

END_POINT = "https://api.openweathermap.org/data/2.8/onecall"
API_KEY = "38dc2958b89574310a17b854ec6aed17"
ACCOUNT_SID = "account_sid"
AUTH_TOKEN = "auth_token"
lat_orlov = 58.538460
lon_orlov = 48.890770

parameters = {
    "lat": lat_orlov,
    "lon": lon_orlov,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"  # Excluimos los datos de que no nos interesan de la API
}

response = requests.get(END_POINT, params=parameters)
response.raise_for_status()
datos = response.json()
datos_horas = datos['hourly'][:13]  # Cortamos el diccionario para recoger las primeras 12 horas

llueve = False  # Si llueve cambiamos a True y solo lo imprimimos una vez.
for tiempo in datos_horas:
    if tiempo['weather'][0]['id'] < 700:  # Según los 'id' de la API, si esta entre 1xx y 7xx es posible que haga
        llueve = True  # falta paraguas

if llueve:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)  # Realizamos la conexión para enviar el sms
    message = client.messages \
        .create(
            body="Coge un paraguas que llueve!!!!",
            from_='+17622525735',
            to='your phone'
        )

    print(message.status)

from requests.auth import HTTPBasicAuth

import config as co
import requests
import datetime as dt

fecha_actual = dt.datetime.now()  # Recogemos la fecha actual para el Sheets

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers_nutritionix = {  # Cabecera para nutritionix
    "x-app-id": co.APP_ID,
    "x-app-key": co.APY_KEY
}

exercise_params = {
    "query": input("Que has hecho hoy?: "),  # Este es el requerido, los demás son opcionales
    "gender": "male",
    "weight_kg": 90,
    "height_cm": 180,
    "age": 40
}

response = requests.post(url=nutritionix_endpoint, json=exercise_params, headers=headers_nutritionix)
result = response.json()
# print(result)

sheety_endpoint = co.END_POINT

sheety_params = {  # Estas son las columnas del sheets
    "workout": {
        "date": fecha_actual.strftime("%d/%m/%Y"),
        "time": fecha_actual.strftime("%H:%M:%S"),
        "exercise": result['exercises'][0]['name'].title(),
        "duration": result['exercises'][0]['duration_min'],
        "calories": result['exercises'][0]['nf_calories']
    }
}

basic = HTTPBasicAuth(co.USER_SHEETY, co.PASSWORD_SHEETY) # Authentication Sheety

response = requests.post(url=sheety_endpoint, json=sheety_params, auth=basic)

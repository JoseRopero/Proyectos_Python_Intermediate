import datetime as dt
import os
import pandas
import random
import smtplib

#  --------------------------- Extra Hard Starting Project ------------------------------- #

MY_EMAIL = "pruebapython83@gmail.com"
PASSWORD = "password"

# 2. Check if today matches a birthday in the birthdays.csv

fecha_actual = dt.datetime.now()  # Obtenemos la fecha actual
datos = pandas.read_csv("birthdays.csv")  # Cargamos el csv
datos_dic = datos.to_dict(orient='records')
directorio = 'letter_templates'
txt_files = [file for file in os.listdir(directorio) if file.endswith('.txt')]  # Listado con los .txt
archivo_random = random.choice(txt_files)  # Elegimos uno al azar
ruta_completa = os.path.join(directorio, archivo_random)  # Cargamos la ruta completa del archivo random

for fecha in datos_dic:  # Recorremos el diccionario para comprobar las fechas con las de hoy
    if fecha_actual.month == fecha['month'] and fecha_actual.day == fecha['day']:
        with open(ruta_completa) as carta:  # Abrimos la carta para reemplazar el nombre
            contenido = carta.read()
            felicitacion = contenido.replace('[NAME]', fecha['name'])
            with smtplib.SMTP("smtp.gmail.com") as connection:  # Realizamos la conección para mandar la carta
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=fecha['email'],
                                    msg=f"Subject:Happy birthday\n\n{felicitacion}")

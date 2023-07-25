import time
from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    # Cargamos el csv con las palabras que nos quedan por aprender. Tenemos que capturar el error porque la primera vez
    # que se ejecuta el programa este archivo no existe.
    datos = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    datos = pandas.read_csv("data/french_words.csv")
finally:
    df = pandas.DataFrame(datos)
    df_dic = df.to_dict(orient="records")  # Convertimos el DataFrame a diccionario.
    random_dic = {}  # Creamos un diccionario vacio para guardar la eleccion random y poder usarla en las dos funciones.


def random_word():
    global random_dic, tiempo_vuelta
    windows.after_cancel(tiempo_vuelta)  # Para que cada vez que pulsemos el botón se cancele los 3 segundos.
    random_dic = random.choice(df_dic)
    canvas.itemconfigure(french_text, text="French", fill="black")
    canvas.itemconfigure(palabra_text, text=random_dic['French'], fill="black")
    canvas.itemconfigure(front_img, image=card_front_img)
    tiempo_vuelta = windows.after(3000, func=voltear_card)


def is_know():  # Si pulsamos el botón verde, eliminamos la palabra del diccionario y guardamos en el csv nuevo
    df_dic.remove(random_dic)
    df_learn = pandas.DataFrame(df_dic)
    df_learn.to_csv("data/words_to_learn.csv", index=False)
    # Nueva carta
    random_word()


def voltear_card():  # Al voltear la carta cambiamos la imagen y traducción
    canvas.itemconfigure(front_img, image=card_back_img)
    canvas.itemconfigure(french_text, text="English", fill="white")
    canvas.itemconfigure(palabra_text, text=random_dic['English'], fill="white")


# -------------------------------------- UI SETUP ------------------------------------------- #


windows = Tk()
windows.title("Flash cards")
windows.config(pady=50, padx=50, background=BACKGROUND_COLOR)

tiempo_vuelta = windows.after(3000, voltear_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
front_img = canvas.create_image(400, 263, image=card_front_img)
french_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
palabra_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
button_wrong = Button(image=wrong_img, highlightthickness=0, command=random_word)
button_wrong.grid(column=0, row=1)
right_img = PhotoImage(file="images/right.png")
button_right = Button(image=right_img, highlightthickness=0, command=is_know)
button_right.grid(column=1, row=1)

random_word()  # Para que al abrir el programa aparezca una palabra al azar.

windows.mainloop()

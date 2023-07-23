import json  # dump: escritura; load: lectura; update: actualizar.
from tkinter import *
from tkinter import messagebox
import random
import pyperclip  # Para copiar en el portapapeles


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)  # Elige un número entre el 8 y el 10
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    lista_letras = [random.choice(letters) for letra in range(nr_letters)]
    lista_letras += [random.choice(numbers) for numeros in range(nr_numbers)]
    lista_letras += [random.choice(symbols) for simbolos in range(nr_symbols)]

    random.shuffle(lista_letras)  # Mezclamos la lista.
    password_final = "".join(lista_letras)  # Unimos cada elemento de la lista sin espacios creando una cadena

    entry_password.insert(0, password_final)

    pyperclip.copy(password_final)  # Copiamos la contraseña generada en el portapapeles.


def save():
    web = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()
    # Creamos un diccionario para el json
    new_data = {
        web: {
            "email": email,
            "password": password,
        }
    }

    if len(web) == 0 or len(email) == 0 or len(password) == 0:  # Para comprobar que no se dejen ningún campo vacio
        messagebox.showwarning(title="Oops", message="Please don´t leave any fields empty!!")
    else:
        try:  # Capturamos el error si el archivo json no existe.
            with open("data.json", "r") as file:
                # Leemos los datos antiguos
                datos = json.load(file)

        except FileNotFoundError:  # Si no existe el json lo creamos con los datos introducidos y salta al finally
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Si no hay ningún error en el try, actualizamos los datos antiguos con los nuevos datos introducidos
            datos.update(new_data)

            with open("data.json", "w") as file:
                # Guardamos los datos actualizados
                # Los parámetros de dump son los datos que queremos volcar y el archivo de datos que queremos poner.
                json.dump(datos, file, indent=4)  # indent es para ver mejor el archivo json
        finally:
            # En cualquier caso limpiamos las entradas.
            entry_web.delete(0, END)
            entry_password.delete(0, END)


def find_password():
    web = entry_web.get()

    if len(web) == 0:  # Para comprobar que ha escrito algo para buscar
        messagebox.showwarning(title="Oops", message="Por favor, introduzca un sitio válido")
    else:
        try:
            with open("data.json", "r") as file:
                datos = json.load(file)
        except FileNotFoundError:
            messagebox.showwarning(title="Oops", message="El listado esta vacío")
        else:
            if web in datos:
                email = datos[web]['email']
                password = datos[web]['password']
                messagebox.showinfo(title=web, message=f"EMail: {email}\nPassword: {password}")
            else:
                messagebox.showwarning(title=web, message="Sitio web no encontrado")
        finally:
            entry_web.delete(0, END)


# -----------------------------  UI SETUP -------------------------------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_web = Label(text="Website:")
label_web.grid(column=0, row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_web = Entry(width=27)
entry_web.focus()
entry_web.grid(column=1, row=1)  # Con columnspan le indicamos el número de columnas que va a ocupar

entry_email = Entry(width=45)
entry_email.insert(0, "jose@jose.com")
entry_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=27)
entry_password.grid(column=1, row=3)

button_search = Button(text="Search", width=14, command=find_password)
button_search.grid(column=2, row=1)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)

window.mainloop()

from tkinter import *
from tkinter import messagebox
import random


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

    random.shuffle(lista_letras)
    password_final = "".join(lista_letras)

    entry_password.insert(0, password_final)


def save():
    web = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(web) == 0 or len(email) == 0 or len(password) == 0:  # Para comprobar que no se dejen ningún campo vacio
        messagebox.showwarning(title="Oops", message="Please don´t leave any fields empty!!")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered:\nEmail: {email}\n"
                                                          f"Password: {password}\nIs it ok save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(web + " | " + email + " | " + password + "\n")
            entry_web.delete(0, END)
            entry_password.delete(0, END)


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

entry_web = Entry(width=45)
entry_web.focus()
entry_web.grid(column=1, row=1, columnspan=2)  # Con columnspan le indicamos el número de columnas que va a ocupar

entry_email = Entry(width=45)
entry_email.insert(0, "jose@jose.com")
entry_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=27)
entry_password.grid(column=1, row=3)

button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(column=2, row=3)

button_add = Button(text="add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()

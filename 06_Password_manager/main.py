from tkinter import *


def save():
    web = entry_web.get()
    email = entry_email.get()
    password = entry_password.get()
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
entry_web.grid(column=1, row=1, columnspan=2)

entry_email = Entry(width=45)
entry_email.insert(0, "jose@jose.com")
entry_email.grid(column=1, row=2, columnspan=2)

entry_password = Entry(width=27)
entry_password.grid(column=1, row=3)

button_generate = Button(text="Generate Password")
button_generate.grid(column=2, row=3)

button_add = Button(text="add", width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2)


window.mainloop()

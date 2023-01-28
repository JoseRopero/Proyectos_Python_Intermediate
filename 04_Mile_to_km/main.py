from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


def miles_to_km():
    miles = float(entrada.get())
    resultado = round(miles * 1.609, 2)
    return label4.config(text=f"{resultado}")


label1 = Label()
label1.grid(column=0, row=0)
label1.config(padx=50, pady=10)

entrada = Entry(width=7)
entrada.insert(END, string="0")
entrada.grid(column=1, row=0)

label2 = Label(text="Miles")
label2.grid(column=2, row=0)
label2.config(padx=20)

label3 = Label(text="is equal to:")
label3.config(pady=10)
label3.grid(column=0, row=1)

label4 = Label(text="0")
label4.grid(column=1, row=1)

label5 = Label(text="Km")
label5.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()

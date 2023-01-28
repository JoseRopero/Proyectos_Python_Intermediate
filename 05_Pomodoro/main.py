from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

# Para poder insertar una imagen en nuestra ventana como fondo usamos Canva()
# Le damos al lienzo unas medidas parecidas a la imagen a insertar
# Con 'highlightthickness=' podemos editar el borde del lienzo, a 0 los quitamos.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# La etiqueta 'image=' del método create_image espera un PhotoImage, una clase de tkinter.
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # Le damos una posición central al lienzo
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()


window.mainloop()

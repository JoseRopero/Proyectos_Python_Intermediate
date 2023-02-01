import math
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
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    label1.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    label2.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        label1.config(text="Work", fg=GREEN)
        count_down(work_sec)  # Llamamos a la función recursiva para iniciar la cuenta atrás.
    if reps == 8:
        label1.config(text="Break", fg=RED)
        count_down(long_break_sec)
    if reps == 2 or reps == 4 or reps == 6:
        label1.config(text="Break", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)  # Devuelve el máximo entero menor o igual a un número.
    count_sec = count % 60
    if count_sec < 10:  # Para formatear la cadena y que en vez de salir 5:0 o 0:9 salga 5:00 y 0:09
        count_sec = f"0{count_sec}"

    # after -> Primero, cantidad de tiempo de espera en milisegundos, después una función a la que llamar,
    # seguido de parámetros para la función. Todos los que queramos.
    # En este caso usaremos una función recursiva bajando el 'count'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:  # Para que no siga bajando hasta los negativos
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✓"
        label2.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

label1 = Label(text="Timer", font=(FONT_NAME, 40, "italic"))
label1.config(fg=GREEN, bg=YELLOW, highlightthickness=0)
label1.grid(column=1, row=0)

button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.grid(column=2, row=2)

label2 = Label()
label2.config(fg=GREEN, bg=YELLOW)
label2.grid(column=1, row=3)

# Para poder insertar una imagen en nuestra ventana como fondo usamos Canva()
# Le damos al lienzo unas medidas parecidas a la imagen a insertar
# Con 'highlightthickness=' podemos editar el borde del lienzo, a 0 los quitamos.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# La etiqueta 'image=' del método create_image espera un PhotoImage, una clase de tkinter.
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # Le damos una posición central al lienzo
# El texto lo metemos en una variable para poder acceder a ella y cambiar el contador.
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.grid(column=0, row=2)

window.mainloop()

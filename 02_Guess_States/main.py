import turtle

import pandas

s = turtle.Screen()
s.title("U.S. States Game")
image = "blank_states_img.gif"
s.addshape(image)  # Cargamos la imagen como forma de la tortuga.
turtle.shape(image)
datos_states = pandas.read_csv("50_states.csv")


def ventana_guess(number):
    return s.textinput(title=f"{number}/50 States Correct", prompt="What´s another state´s name?").title()


def check_guess(states):
    if states in datos_states.state.values:  # Comprueba que el estado introducido esté en el csv.
        return True
    else:
        return False


def pintar_state(nombre_state):
    row = datos_states[datos_states.state == nombre_state]
    coor_x = int(row.x)
    coor_y = int(row.y)
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(coor_x, coor_y)
    t.write(arg=f"{nombre_state}", move=False, align='center', font=('Courier', 8, 'normal'))


def generar_csv(lista):
    lista_estados = datos_states.state.to_list()
    lista_aprender = set(lista_estados) - set(lista)
    datos_estados = pandas.DataFrame(lista_aprender).sort_values(0)  # Ordenamos por el nombre.
    datos_estados.to_csv("estados_estudiar.csv")


lista_states = []
contador = 0
while contador < 50:
    respuesta = ventana_guess(contador)
    if respuesta == "Exit":
        break
    if respuesta not in lista_states:
        if check_guess(respuesta):
            lista_states.append(respuesta)
            print(lista_states)
            pintar_state(respuesta)
            contador += 1
generar_csv(lista_states)

turtle.exitonclick()

"""
Función para imprimir las coordenadas donde hacemos click con el ratón. Para completar el csv con los 50 estados

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)  # onscreenclick evento para escuchar al ratón.
"""

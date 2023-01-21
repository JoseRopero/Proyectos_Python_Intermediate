
with open("./Input/Names/invited_names.txt") as invitados:  # Pasamos el txt de los invitados a una lista
    nombres = invitados.readlines()  # Pasa las líneas como elementos de una lista, pero con un salto de línea


with open("./Input/Letters/starting_letter.txt") as carta:
    contenido = carta.read()  # Leemos la plantilla
    for nombre in nombres:  # Recorremos la lista creada y quitamos los saltos de línea de cada nombre
        nombre_final = nombre.strip()
        contenido_final = contenido.replace('[name]', nombre_final)  # Creamos el contenido de la carta
        with open(f"./Output/ReadyToSend/letter_for_{nombre_final}.txt", 'w') as carta_final:
            carta_final.write(contenido_final)

# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as invitados:  # Pasamos el txt de los invitados a una lista
    nombres = invitados.readlines()  # Pasa las líneas como elementos de una lista, pero con un salto de línea


with open("./Input/Letters/starting_letter.txt") as carta:
    contenido = carta.read()  # Leemos la plantilla
    for nombre in nombres:  # Recorremos la lista creada y quitamos los saltos de línea de cada nombre
        nombre_final = nombre.strip()
        contenido_final = contenido.replace('[name]', nombre_final)  # Creamos el contenido de la carta
        with open(f"./Output/ReadyToSend/letter_for_{nombre_final}.txt", 'w') as carta_final:
            carta_final.write(contenido_final)

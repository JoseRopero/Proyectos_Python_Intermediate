import pandas

datos = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(datos)

# Creamos el diccionario a partir del dataframe.
datos_dic = {row.letter: row.code for (index, row) in df.iterrows()}

# Pedimos una palabra y la convertimos a mayúsculas para después crear una lista con los caracteres

bandera = True
while bandera:
    try:
        palabra = input("Introduzca una palabra para deletrear: ").upper()
        lista_palabra = [letra for letra in palabra]
        # Guardamos en una lista el valor del diccionario utilizando de key el carácter de la palabra.
        # Si no se encuentra capturamos el error y hacemos que repita hasta que introduzca una palabra válida
        lista_otan = [datos_dic[letter] for letter in lista_palabra]
        print(lista_otan)
    except KeyError as mensaje:
        print(f"{mensaje} no es válida. Por favor introduzca una palabra válida")
    else:
        bandera = False


# Otra manera de manejar el error y que siga pidiendo una palabra válida es con una función

# def phonetic():
#      palabra = input("Introduzca una palabra para deletrear: ").upper()
#      lista_palabra = [letra for letra in palabra]
#      # Guardamos en una lista el valor del diccionario utilizando de key el carácter de la palabra.
#      # Si no se encuentra capturamos el error y hacemos que repita hasta que introduzca una palabra válida
#      try:
#          lista_otan = [datos_dic[letter] for letter in lista_palabra]
#      except KeyError as mensaje:
#          print(f"{mensaje} no es válida. Por favor introduzca una palabra válida")
#          En este paso hacemos que se repita hasta que pongamos una palabra válida
#          phonetic()
#      else:
#          print(lista_otan)
# phonetic()





import pandas

datos = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(datos)

# Creamos el diccionario a partir del dataframe.
datos_dic = {row.letter: row.code for (index, row) in df.iterrows()}

# Pedimos una palabra y la convertimos a mayúsculas para después crear una lista con los caracteres
palabra = input("Introduzca una palabra para deletrear: ").upper()
lista_palabra = [letra for letra in palabra]

# Guardamos en una lista el valor del diccionario utilizando de key el carácter de la palabra.
lista_otan = [datos_dic[letter] for letter in lista_palabra]
print(lista_otan)

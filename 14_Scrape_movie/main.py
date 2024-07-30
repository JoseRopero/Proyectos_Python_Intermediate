from bs4 import BeautifulSoup
import requests

# Primero guardamos en una variable el HTML de la página.
response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best'
                        '-movies-2/')
web_movies = response.text

# Analizamos el HTML
soup = BeautifulSoup(web_movies, 'html.parser')

# Inspeccionamos el HTML y cogemos la línea que nos interesa
titles = soup.find_all(name='h3', class_='title')

# Recorremos el listado para sacar solo el texto e invertirlo
names_titles = []
for name in titles:
    names_titles.append(name.getText())
titles_reverse = names_titles[::-1]

# Creamos un txt con el listado
with open('movies.txt', mode='w', encoding='utf-8') as file:
    for titulo in titles_reverse:
        file.write(f'{titulo}\n')

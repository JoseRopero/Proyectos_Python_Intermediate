from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import config as c
# import pprint

# Realizamos la autenticación con Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-private', redirect_uri='http://example.com',
                                               client_id=c.CLIENT_ID, client_secret=c.CLIENT_SECRET, show_dialog=True,
                                               cache_path='token.txt', username=c.USERNAME))

# Guardamos el ID de usuario autenticado para más tarde crear la playlist
user_id = sp.current_user()['id']

# Preguntamos por la fecha que quieres ver las 100 canciones y guardamos los titulos
fecha = input('A que fecha quieres viajar? Escribe la fecha en este formato YYYY-MM-DD:')

URL = f'https://www.billboard.com/charts/hot-100/{fecha}/'

response = requests.get(URL)
web_billboard = response.text

soup = BeautifulSoup(web_billboard, 'html.parser')

titles = soup.select('li .o-chart-results-list__item h3')

print('\n\t\t\tLos titulos que mas se escucharon fueron:\n')
names_titles = []
for name in titles:
    names_titles.append(name.getText().strip())
    print(name.getText().strip())

# Ahora buscamos los titulos de las canciones por el año que elegimos en Spotify
print('\n\t\t\t Creando Playlist y añadiendo canciones...\n')
song_uris = []
year = fecha.split('-')[0]
for song in names_titles:
    result = sp.search(q=f'track:{song} year:{year}', type='track')
    # result = sp.search(q=f'track:{song}', type='track')
    # print(result)
    # pprint.pp(result)
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
        print(f'{song}, AÑADIDA')
    except IndexError:
        print(f'{song} no existe en Spotify, SKIPPED')

# Creamos la playlist
playlist = sp.user_playlist_create(user=user_id, name=f'{fecha} Billboard 100', public=False, collaborative=False,
                                   description='Billboard 100')
# print(playlist)

# Guardamos el ID de la playlist para añadir canciones
playlist_id = playlist['id']

# Añadimos las canciones que antes hemos buscado
sp.playlist_add_items(playlist_id, song_uris)

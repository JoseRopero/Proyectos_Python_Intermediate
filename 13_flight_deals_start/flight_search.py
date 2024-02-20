import config
import requests
from flight_data import FlightData
from pprint import pprint


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def get_destination_code(self, city):
        # Realizamos la llamada segun las especificaciones de la API
        location_endpoint = f'{config.END_POINT_TEQUILA}/locations/query'
        headers = {
            'apikey': config.KEY_TEQUILA
        }
        query = {
            'term': city,
            'location_types': 'city'
        }

        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()['locations']
        code = results[0]['code']  # Nos quedamos con el código
        return code

    def get_prices(self, origin_city_code, destination_city_code, from_time, to_time):  # Buscador de vuelos
        header = {
            'apikey': config.KEY_TEQUILA
        }

        query = {  # Seguimos las especificaciones de la API
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime('%d/%m/%Y'),
            'date_to': to_time.strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'one_for_city': 1,
            'max_stopovers': 0,
            'curr': 'GBP'
        }

        response = requests.get(url=f'{config.END_POINT_TEQUILA}/search', headers=header, params=query)

        try:
            data = response.json()['data'][0]

        except IndexError:
            print(f'No hay vuelos para {destination_city_code}.')
            return None

        flight_data = FlightData(  # Inicializamos el constructor con todos los datos
            price=data['price'],
            origin_city=data['route'][0]['cityFrom'],
            origin_airport=data['route'][0]['flyFrom'],
            destination_city=data['route'][0]['cityTo'],
            destination_airport=data['route'][0]['flyTo'],
            out_date=data["route"][0]["dTime"],
            return_date=data['route'][1]['aTime']
        )

        print(f'{flight_data.destination_city}: {flight_data.price}')  # imprimimos el precio
        return flight_data

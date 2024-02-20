import config
import requests


class DataManager:
    def __init__(self):  # Constructor para almacenar todos los datos del sheet
        self.destination_data = {}

    def get_destination_data(self):  # Hacemos la llamada a la API para recoger los datos del sheet
        response = requests.get(url=config.END_POINT)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def put_destination_data(self):
        for city in self.destination_data:  # Recorremos cada fila y recogemos el dato de iataCode.
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{config.END_POINT}/{city['id']}",  # Realizamos el put para actualizar el iataCode del sheet
                json=new_data
            )

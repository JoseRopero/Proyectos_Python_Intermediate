# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager


data_manager = DataManager()  # Inicializamos el data_manager para el sheet
sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
notification = NotificationManager()


if sheet_data[0]['iataCode'] == "":  # Si la columna esta vacía importamos para recoger los codigos de la ciudad
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])

    data_manager.destination_data = sheet_data
    data_manager.put_destination_data()

tomorrow = datetime.now() + timedelta(days=1)  # Para buscar vuelos entre mañana y 6 meses
six_month = tomorrow + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.get_prices(  # Buscamos los vuelos con los parametros introducidos
        'LON',
        destination['iataCode'],
        from_time=tomorrow,
        to_time=six_month
    )

    # Si el precio es menor que el que tenemos en el sheet enviamos el sms.
    if flight.price < destination['lowestPrice']:
        notification.send_sms(
            message=f'Alerta de precio. Solo {flight.price} libras volar desde {flight.origin_city}-'
                    f'{flight.origin_airport} a {flight.destination_city}-{flight.destination_airport}'
        )




from twilio.rest import Client
import config


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    # Constructor para la conexion con el cliente.
    def __init__(self):
        self.client = Client(config.TWILIO_SID, config.TWILIO_AUTH_TOKEN)

    # Envio del sms
    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=config.TWILIO_PHONE_VIRTUAL,
            to=config.TWILIO_PHONE,
        )
        # Imprimimos si el sms fue enviado
        print(message.sid)

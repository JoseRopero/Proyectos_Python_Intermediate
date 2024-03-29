from twilio.rest import Client
import config
import smtplib


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

    # Envio de correos a todos los usuarios.
    def send_email(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:  # Realizamos la conección para mandar los correos
            connection.starttls()
            connection.login(user=config.MY_EMAIL, password=config.PASSWORD_EMAIL)
            for email in emails:  # Por cada email realizamos un envio
                connection.sendmail(from_addr=config.MY_EMAIL,
                                    to_addrs=email,
                                    msg=f"Subject:Ofertas de vuelos\n\n{message}")


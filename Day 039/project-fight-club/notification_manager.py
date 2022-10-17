from twilio.rest import Client

TWILIO_SID = 'AC6039a7fe299031fb85f652d3a9b40515'
TWILIO_AUTH_TOKEN = '6457d2bcc2977d22b00012b37ad110f5'
TWILIO_VIRTUAL_NUMBER = '+13857072715'
TWILIO_VERIFIED_NUMBER = '+84352863102'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

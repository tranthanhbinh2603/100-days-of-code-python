from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def SendSMS(self, city_to, iata_to, price):
        account_sid = 'AC6039a7fe299031fb85f652d3a9b40515'
        auth_token = '6457d2bcc2977d22b00012b37ad110f5'
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"Low price alert! Only £{price} to fly from London-STN to {city_to}-{iata_to}",
            from_='+13857072715',
            to='+84352863102'
        )

        print(message.sid)
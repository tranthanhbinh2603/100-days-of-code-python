from requests import *
SHEETY_GETLINK = 'https://api.sheety.co/3bbc8e294f7b6a69e668615a446142c8/flightDeals/prices'

class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self):
        self.sheet_data = []

    def GetData(self):
        data = get(url=SHEETY_GETLINK).json()
        for row in data['prices']:
            self.sheet_data.append(row)
        return self.sheet_data


    def PutData(self):
        for index in range(0, len(self.sheet_data)):
            PostLink = f'{SHEETY_GETLINK}/{index + 2}'
            body = {
                'price':{
                    'iataCode': self.sheet_data[index]['iataCode']
                }
            }
            print(put(url=PostLink, json=body).text)

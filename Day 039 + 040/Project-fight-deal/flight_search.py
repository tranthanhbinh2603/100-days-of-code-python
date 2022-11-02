from requests import *
from datetime import *

SHEETY_OUTPOINT = 'https://api.tequila.kiwi.com'
API_KEY = 'WE9nWc2-jqva0Wmpo8kgDGH_3MTZso05'

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass

    def Search(self, from_city, to_city):
        #Có dùng hàm timedelta để cộng thêm ngày
        param = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y"),
            "date_to": (datetime.now() + timedelta(days=(6 * 30))).strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        header = {
            'apikey': API_KEY
        }
        link = f'{SHEETY_OUTPOINT}/search'
        return get(url=link, headers=header, params=param).json()['data'][0]['conversion']['GBP']


    def getIATACode(self, cityname):
        link = f'{SHEETY_OUTPOINT}/locations/query'
        header = {
            'apikey': API_KEY
        }
        param = {
            'term': cityname,
            'location_types': 'city'
        }
        return get(url=link, headers=header, params=param).json()['locations'][0]['code']







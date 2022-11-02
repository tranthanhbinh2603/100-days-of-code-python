#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_search import *
from data_manager import *
from flight_data import *
from notification_manager import *
from pprint import pprint #Thư viện in đẹp

flightsea = FlightSearch()
data_object = FlightData()

data_object.GetData()

for item in data_object.sheet_data:
 if item['iataCode'] == '':
  item['iataCode'] = flightsea.getIATACode(item['city'])

#data_object.PutData()
lowest_price = 0
lowest_city = ''
lowest_iata = ''
count = 1
for item in data_object.sheet_data:
    #print(f'{item["city"]}: ${flightsea.Search("LON", item["iataCode"])}')
    if count == 1:
        lowest_price = int(flightsea.Search("LON", item["iataCode"]))
        lowest_city = item["city"]
        lowest_iata = item["iataCode"]
        count += 1
        continue
    price = int(flightsea.Search("LON", item["iataCode"]))
    if price < lowest_price:
        lowest_price = price
        lowest_city = item["city"]
        lowest_iata = item["iataCode"]
    count += 1

noti = NotificationManager()
noti.SendSMS(lowest_city, lowest_iata, lowest_price)

#data.PutData(sheet_data)
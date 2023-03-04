#TODO 1:
#TODO 2:

import requests
from bs4 import BeautifulSoup
import lxml

#https://www.amazon.com/Furinno-Hermite-Organizing-Bookcase-Espresso/dp/B09YJ44STS/

#Get header: myhttpheader.com
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Accept-Language' : 'vi,vi-VN;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5'}

s = requests.get('https://www.amazon.com/Furinno-Hermite-Organizing-Bookcase-Espresso/dp/B09YJ44STS/', headers=header)
soup = BeautifulSoup()
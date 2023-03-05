#TODO 1: Get link bên Amazon
#TODO 2: Dùng Beautiful Soup để thực hiện lấy tiêu đề và giá
#TODO 3: Nếu giá nhỏ hơn giá mình cần mua thì thực hiện gửi mail cảnh báo

#NOTE 1: Ôn tập cách gửi mail
#NOTE 2: Sử dụng lxml thay cho html.parser

import requests
from bs4 import BeautifulSoup
from smtplib import *
import lxml

#https://www.amazon.com/Furinno-Hermite-Organizing-Bookcase-Espresso/dp/B09YJ44STS/

#Get header: myhttpheader.com
header = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Accept-Language' : 'vi,vi-VN;q=0.9,en-US;q=0.8,en;q=0.7,fr-FR;q=0.6,fr;q=0.5'}

link = 'https://www.amazon.com/dp/B007BV7J0K/'
s = requests.get(link, headers=header)
#Có lôi: bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: html-parser. Do you need to install a parser library?
soup = BeautifulSoup(s.text, 'lxml')
price = float(str(soup.find('span', {'class': 'a-size-base a-color-base'}).string).strip().replace('$', ''))
name = str(soup.find('span', {'class': 'a-size-large product-title-word-break'}).string).strip()

price_provise = 35
if (price < price_provise):
    my_email = "macketoi0326@gmail.com"
    connection = SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password='ewhmhvbhhswxalev')
    connection.sendmail(from_addr=my_email,
                        to_addrs='leha.tieuhocthanhson@gmail.com',
                        msg=f"Subject:Amazon Price Alert!\n\n{name} is now ${price}\n{link}")
    connection.close()

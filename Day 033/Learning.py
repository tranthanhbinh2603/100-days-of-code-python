# Ví dụ bạn lên hackerrank, nhìn thấy 1 bảng số liệu. Làm sao lấy nó về? Cần có API


# An Application Programming Interface (API) is a set of commands, functions, protocols,and objects
# that programmers can use to create software or interact with an external svstem.

#Tưởng tượng bạn đi vô nhà hàng. Có bao giờ bạn vào thẳng nhà bếp để lấy đồ ăn không? Dĩ nhiên là O.

#Api endpoint

#tiện ích json viewer awesome: https://chrome.google.com/webstore/detail/json-viewer-pro/eifflpmocdbdmepbjaopkkhbfmdgijcc

#Ý nghĩa của JSON: Dễ dàng về lại 1 dict

#Cách để lấy 1 dữ liệu:
# from requests import *
#
# response = get(url='https://sponsor.ajay.app/api/isUserVIP?userID=[%2228940fee320a2ee80f582029a21167cc1b4a383e0fdfaf0c03a42bccc2100327%22]')
# print(response)

#Response code: (https://www.webfx.com/web-development/glossary/http-status-codes/)
# 1XX: Hold On
# 2XX: Here You Go
# 3XX: Go Away
# 4XX You Screwed Up
# 5XX:I Screwed Up

#Get lỗi response:
# from requests import *

# response = get(url='https://sponsor.ajay.app/api/isUserVIP?userID=[%2228940fee320a2ee80f582029a21167cc1b4a383e0fdfaf0c03a42bccc2100327%22]')
# if response.status_code != 200:
#     #print('Có chuyện gì đó')
#     #raise Exception('Hình như có gì đó đéo ổn ở đây')
#     response.raise_for_status()
# else:
#     print('Thành công nè')

#Xem số sao trong PyPI

# from requests import *
# response = get(url='https://sponsor.ajay.app/api/isUserVIP?userID=[%2228940fee320a2ee80f582029a21167cc1b4a383e0fdfaf0c03a42bccc2100327%22]').json()["hashedUserID"]
# print(response)

#API Parameter
#Example
from requests import *
from datetime import *

parameter ={
    "lat": 36.7201600,
    "lng": -4.4203400,
    "formatted": 0
}

# print(get('https://api.sunrise-sunset.org/json', params=parameter).json())
# print(get('https://api.sunrise-sunset.org/json', params=parameter).json()['results'])
# print(get('https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400').json()) #Call para trong link

data = get('https://api.sunrise-sunset.org/json', params=parameter).json()
sunrise = str(data['results']['sunrise']).split('T')[1].split(':')[0]
sunset = data['results']['sunset'].split('T')[1].split(':')[0]
print(f'{sunset} {sunrise} {datetime.now().hour}')

#Xem toạ độ: https://www.latlong.net/Show-Latitude-Longitude.html


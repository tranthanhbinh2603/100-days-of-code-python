from requests import *

API_KEY = '69f04e4613056b159c2761a9d9e664d2'
#Key của tài khoản Angela: 69f04e4613056b159c2761a9d9e664d2

#Vào https://openweathermap.org/home/sign_in, đăng kí tài khoản
#Đăng kí thành công, vào https://home.openweathermap.org/api_keys để lấy api key. Đặt tên tuỳ thich nếu cần
#Lưu ý: Key muốn kích hoạt vui lòng đợi 1 khoảng thời gian.

#Api sử dụng trong bài:
#https://openweathermap.org/current

#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
#Exam: https://api.openweathermap.org/data/2.5/weather?lat=11.225380&lon=107.292160&appid=69f04e4613056b159c2761a9d9e664d2
#Nếu ra lỗi 401 là lỗi authen

#http://jsonviewer.stack.hu/

#Thử thách: https://openweathermap.org/api/one-call-api
#https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}

parameter = {
    'lat': '11.225380',
    'lon': '107.292160',
    'exclude': 'hourly', #Tài khoản miễn phí cho hourly thì phải
    'appid': API_KEY
}

print(get('https://api.openweathermap.org/data/2.5/onecall', params=parameter).json())



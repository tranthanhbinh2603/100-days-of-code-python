#Api theo doi thoi quen hang ngay: Pixela (https://pixe.la/)
#Cách sử dụng: https://docs.pixe.la/

#Request: https://requests.readthedocs.io/en/latest/api/

#Post request: Là sự đưa dữ liệu vào hệ thống khác mà không quan tâm kết quả trả về của hệ thông bên kia (Tuc là chỉ quan tâm lỗi)
#Put request: yêu cầu 1 phần dữ liệu trong bộ dữ liệu lớn
#Delete request: Xoá 1 phần hoặc toàn bộ dữ liệu

from requests import *

user_pra = {
    "token":"pciV5gbbjGrrNnwWgAq1",
    "username":"tranthanhbinh2603",
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

pixela_endpoint = 'https://pixe.la/v1/users'

#Đăng kí tài khoản. Chỉ chạy 1 LẦN DUY NHẤT
# print(post(url=pixela_endpoint, json=user_pra).text)
#Thành công: {"message":"Success. Let's visit https://pixe.la/@tranthanhbinh2603 , it is your profile page!","isSuccess":true}
#Đã trùng: {"message":"This user already exist.","isSuccess":false}

#Tạo 1 mã thông báo tạo 1 trang pixela mới (có trong file project)
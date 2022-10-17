# B1: thực hiện tạo tài khoản
# B2: thực hện tạo biểu đổ
# B3: Post 1 khối (post_pixel)
# B4: Update (put) 1 khối
# B5: delete pixel


from requests import *
from datetime import *

api_key = 'pciV5gbbjGrrNnwWgAq1'
user_name = 'tranthanhbinh2603'

id_graph = 'readbookiseasy'

pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f'{pixela_endpoint}/{user_name}/graphs'
post_pixel_endpoint = f'{pixela_endpoint}/{user_name}/graphs/{id_graph}'
put_pixel_endpoint = f'{pixela_endpoint}/{user_name}/graphs/{id_graph}/{datetime.now().strftime("%Y%m%d")}'
delete_pixel_endpoint = f'{pixela_endpoint}/{user_name}/graphs/{id_graph}/{datetime.now().strftime("%Y%m%d")}'

#Create new graph:https://docs.pixe.la/entry/post-graph

# #Header: Giúp api xác thực dữ liệu
# header = {
#     "X-USER-TOKEN": api_key #MÃ AUTHEN CŨNG LÀ MÃ TOKEN
# }
#
# #Request body:
# request_body = {
#     "id": id_graph,
#     "name": "Đọc sách dễ mà",
#     "unit": "trang",
#     "type": "int", #int or float
#     "color": "ajisai" #"The color you specify must be one of the following: shibafu / momiji / sora / ichou / ajisai / kuro"
# }
#
# Thực hiện post. Chạy 1 lần duy nhất
# print(post(url=graph_endpoint, json=request_body, headers=header).text)
# Vào trang web: https://pixe.la/v1/users/<username>/graphs/<id graph>.html
# Example: https://pixe.la/v1/users/tranthanhbinh2603/graphs/readbookiseasy.html

# #Thực hiện việc điền 1 khối (fill pixel): https://docs.pixe.la/entry/post-pixel
# #Cách cũ
# # datenow = str(datetime.now().year) + \
# #           (str(datetime.now().month) if datetime.now().month >= 10 else '0' + str(datetime.now().month)) + \
# #           (str(datetime.now().day) if datetime.now().day >= 10 else '0' + str(datetime.now().day))
# #Cách mới: https://www.w3schools.com/python/python_datetime.asp#:~:text=The%20strftime()%20Method
# datenow = datetime.now().strftime("%Y%m%d")
#
# header = {
#     "X-USER-TOKEN": api_key,
# }
#
# body = {
#     "date": datenow,
#     #"quantity": "20",
#     #"quantity": input('Nhap so trang ban da doc hang ngay')
#     # "optionalData": {
#     #     "Humm, đọc được 20 trang nha! Không tầm thường đâu"
#     # } #Không có cũng được
# }
#
# #/v1/users/<username>/graphs/<graphID>
# #Thay username và graph ID push
# print(post(url=post_pixel_endpoint, json=body, headers=header).text)

#Update pixel: https://docs.pixe.la/entry/put-pixel
# header = {
#     "X-USER-TOKEN": api_key,
# }
#
# body = {
#     "quantity": "50",
# }
# print(put(url=put_pixel_endpoint, json=body, headers=header).text)

#Delete pixel: https://docs.pixe.la/entry/delete-pixel
header = {
    "X-USER-TOKEN": api_key,
}
print(delete(url=delete_pixel_endpoint, headers=header).text)

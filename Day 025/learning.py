#Cách cũ
# with open('weather_data.csv', mode='r') as f:
#     print(f.readlines())

#Cách 2
# from csv import *
# with open('weather_data.csv', mode='r') as f:
#     data = reader(f.readlines())
#     # for row in data:
#     #     print(row)
#     temperture = []
#     for row in data:
#         if row[1] != 'temp':
#             temperture.append(int(row[1]))
#     print(temperture)

#Cách 3:
#Tham khảo thêm:
# https://pandas.pydata.org/docs/reference/index.html
# https://pandas.pydata.org/docs/
import pandas
from pandas import *
data = read_csv('weather_data.csv')
# print(type(data)) #<class 'pandas.core.frame.DataFrame'> - Dữ liệu 1 bảng - 2 chiều
# print(type(data["temp"])) #<class 'pandas.core.series.Series'> - Dữ liệu 1 chiều - 1 cột
#Có thể chuyển sang 1 dict bằng cách:
data_dict = data.to_dict()
print(data_dict)
data_temp_list = data["temp"].tolist()
print(data_temp_list)
print(sum(data_temp_list) / len(data_temp_list)) #Thử thách tính trung bình
#Một cách khác
print(data["temp"].mean())
#Cũng có thể thử tính max
print(data["temp"].max())
# -----------------------------
print(data.condition)
#Lấy data từ row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

#Lấy 1 ô trong bảng giá trị
monday = data[data.day == "Monday"]
print(monday.temp)
print(f"Do F: {int(monday.temp) * 1.8 + 32}")

#Tạo 1 dataframe:
data_dict = {
    "student": ["A", "B", "C"],
    "score": [34, 35, 32]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")




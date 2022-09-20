from random import *
from pandas import *

# How to Create Lists using List Comprehension
number = [1, 2, 3]
#new_list = [new_item for item in list]
new_list = [n + 1 for n in number]
print(new_list)

#Có thể cho 1 chuỗi chữ
string = "Binh"
new_list_string = [n for n in string]
print(new_list_string)

#Tạo ra 1 mảng mới bẳng range. Sau đó nhân đôi tất cả giá trị
max_range = 10
new_list_number = [n for n in range(1, int(max_range) + 1)]
print(new_list_number)
new_list_number_is_double = [n * 2 for n in new_list_number]
print(new_list_number_is_double)
new_list_number_if = [n for n in new_list_number_is_double if n > 10]
print(new_list_number_if)

#Chanllenge cuối
list_name = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
new_list_name = [str(name).upper() for name in list_name if len(name) > 5]
print(new_list_name)

#Dict Comprehension
list_name = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
dict_score = {student:randint(0, 100) for student in list_name}
print(dict_score)
passed = {name:score for (name, score) in dict_score.items() if score > 60}
print(passed)

#How to Iterate over a Pandas DataFrame
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
#loop:
for (key, value) in student_dict.items():
    print(f"{key} {value}")
#Create datafrime
student_data_frime = DataFrame(student_dict)
#for datafrime:
# for (key, value) in student_data_frime.item():
#     print(value)
for (key, value) in student_data_frime.iterrows():
    if value.student == "Angela":
        print(value.score)



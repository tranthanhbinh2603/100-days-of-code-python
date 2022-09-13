# file = open("myfile.txt")
# content = file.read()
# print(content)
#Cách 1:


#Cách 2:
# with open("myfile.txt") as file:
#     content = file.read()
#     print(content)

#Ghi file:
# with open("myfile.txt", mode='w') as file: #Ghi đè
#     file.write('hahaaahaaaahaha')
# with open("myfilea.txt", mode='a') as file: #Ghi thêm vào file
#     file.write('\nhahaaahaaaahaha')
#Nếu không có file, tự động tạo file.

#Absolute File Path - Đường dẫn tuyệt đối
#Relative File Path - Đường dẫn tương đối

#Vd về đường đẫn tương đối
with open("./Test/myfile.txt", mode='a') as file: #Ghi thêm vào file
    file.write('\n123')


#Đoạn code sau sẽ ra lỗi:
# with open('haha_this_is_catch.txt', mode='r') as f:
#     f.readlines()
#Error: FileNotFoundError: [Errno 2] No such file or directory: 'haha_this_is_catch.txt'

#Một số lỗi:
#KeyError:
# dict = {"aaaa": "bbbbbb"}
# print(dict["non_exist"])

#IndexError:
# list = ["aaa", "bbbb", "cccccc"]
# print(list[3]) #IndexError: list index out of range

#Type error:
# str = "abc"
# print(str + 5)

#Cách bắt lỗi:
# try:
#     #Code sinh ra lỗi
#     with open('haha_this_is_catch.txt', mode='r') as f:
#         f.readlines()
#     dict = {"aaaa": "bbbbbb"}
#     print(dict["non_exist"])
# except FileNotFoundError as error_message:
#     print(f'FileNotFoundError: {error_message}')
# except KeyError:
#     print('KeyError')
# except:
#     #Code chạy nếu đoạn trên lỗi
#     #Đã chạy except trên không chạy được thêm except dưới nữa
#     print('Hình như nó có lỗi')
# else:
#     #Code nếu đoạn trên không lỗi
#     print('Hehe, code này không lỗi')
# finally:
#     #Code trên có lỗi hay không nó cũng chạy
#     print('Tui thích hiện lên vậy đó.')
#     #Có thể là đọc file
#     #Có thể tạo ra 1 lỗi của chính bản thân mình:
#     raise KeyError("Heheheehehehehehehe")


#Một ví dụ khác về việc tạo lỗi
a = int(input('ĐỪNG NHẬP LỚN HƠN 30: '))
if a > 30:
    raise ValueError('Nói rồi, đừng nhập lớn hơn 30')

#1. Func have agrument default
# def Sum(a, b = 2, c = 10):
#     return a + b + c
#
# print(Sum(1, 3))
# print(Sum(3)) #a=3, b=2
# print(Sum(5, b=8)) #a=5, b=8


#2. Many Positional Arguments - Nhận các đối số không tên
# def Sum(*args):
#     #print(args)
#     #print(type(args)) #Day là 1 tuple
#     sum = 0
#     for i in args:
#         #print(i)
#         sum += int(i)
#     return sum
#
# print(Sum(1, 2, 3, 4, 5))
# print(Sum(1, 2, 7))

#3. Many Keyword Arguments - Nhận các đối số có tên:
# def Func_not_name(**kwargs):
#     # print(kwargs)
#     # print(type(kwargs)) #Day la 1 dict
#     print(kwargs["c"])
#     sum = 0
#     for (key, value) in kwargs.items():
#         #print(f"{key} {value}")
#         if key == 'a':
#             sum += value
#         if key == 'b':
#             sum += value * 2
#         if key == 'c':
#             sum += value * value
#     return sum
#
# print(Func_not_name(a=1, b=2, c=3))

#3.2: Mở rộng cho OOP:
class Car:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.score = kwargs["score"]

class Car_not_error:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.score = kwargs.get("score")

car = Car(name="Tran Thanh Binh", score="10000")
#Các đối số bắt buộc phải có, vd: car2 = Car(name="Hacker")
car2 = Car_not_error(name = "Hacker")
print(f"{car.name}\n{car.score}")
print(f"{car2.name}\n{car2.score}")


def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)
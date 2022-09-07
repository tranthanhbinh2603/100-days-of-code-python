class animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print('Ăn, uống')

class Fish(animal):
    def __init__(self):
        super().__init__()
        # pass

    def swim(self):
        print('Đi bơi thôi!')

    def breathe(self):
        super(Fish, self).breathe()
        print('====>Làm ở dưới nước')

nemo = Fish()
nemo.breathe()
nemo.swim()
print(nemo.num_eyes)


#Sliceing
piano_key = ["a", "b", "c", "d", "e", "f", "g"]
#           0   1    2    3    4    5    6    7
#Nó theo lát chia
print(piano_key[2:5])
print(piano_key[0:7:2])
print(piano_key[::2]) #Dòng này y như dòng trên
print(piano_key[::-1]) #Đảo ngược mảng trong python
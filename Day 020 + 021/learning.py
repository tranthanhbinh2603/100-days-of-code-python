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
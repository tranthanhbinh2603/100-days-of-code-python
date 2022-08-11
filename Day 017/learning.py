class User:
    #Contructer
    def __init__(self, id, userName):
        print('New user is created.....')
        self.id = id
        self.userName = userName
        self.follower = 0
        self.following = 0
    def notthingFunction(self):
        pass #Bỏ qua hàm
    def follow(self, user):
        user.follower += 1
        self.following += 1
    pass


# user1 = User()
# user1.id = '01'
# user1.userName = "tranthanhbinh"
# print(f"{user1.id} {user1.userName}") #Có thể gọi không cần hàm khởi tạo
#
# user2 = User()
# user2.id = "02"
# user2.userName = "Jack"
# print(f"{user2.id} {user2.userName}") #Có thể gọi không cần hàm khởi tạo

user1 = User("01", "tranthanhbinh")
user2 = User("02", "jack")
print(f"{user1.id} {user1.userName}")
print(f"{user2.id} {user2.userName}")
user1.follow(user2)
print(user1.follower)
print(user1.following)
print(user2.follower)
print(user2.following)
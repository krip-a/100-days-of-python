class User:
    #pass to skip 
    def __init__(self, user_id, username):
        #to initialize attributes
        #print("new user being created...")
        self.id = user_id
        self.username = username
        self.followers = 0 #default
        self.following = 0

    #methods
    def follow(self, user):           #method always needs self to be the first parameter
        user.followers += 1
        self.following += 1


user1 = User("001", "angela")
#user1.id = "001"
#user1.username = "angela"

user2 = User("002", "jack")
#user2.id = "002"
#user2.username = "jack"

user1.follow(user2)
print(user1.followers)
print(user1.following)

print(user2.followers)
print(user2.following)



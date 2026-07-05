class User:

    def __init__(self):
        self.id = 0
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        self.following += 1
        user.followers += 1

user1 = User()
user2 = User()

user1.follow(user2)
user2.follow(user1)

print(f"User 1 followers: {user1.followers}")
print(f"User 1 following: {user1.following}")
print(f"User 2 followers: {user2.followers}")
print(f"User 2 following: {user2.following}")

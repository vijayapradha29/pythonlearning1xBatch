#public variable:

class Myclass:
    def __init__(self):
        self.public=10
        # self.public_var=10
    def public_method(self):
        print("This is a Public Method")

obj1=Myclass()
obj2=Myclass()
# print(obj1.public_var)
print(obj1.public)
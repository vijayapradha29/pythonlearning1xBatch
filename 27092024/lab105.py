#private variable:

class Myclass:
    def __init__(self):
        self.public=10
        self._protected=30
        self.__private=50
    def public_method(self):
        print("This is a Public Method")
        print(obj1.__private)
    def protected_method(self):
        print("Protected Variable")
        print("This is visible inside the class only",self.__private)
    def private_method(self):
        print("Private Method")
obj1=Myclass()
obj2=Myclass()
print(obj1.public)
print(obj2._protected)

obj1.public_method()
obj2.protected_method()
obj1.private_method()
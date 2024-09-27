#protected variable:

class Myclass:
    def __init__(self):
        self.public=10
        self._protected=30
    def public_method(self):
        print("This is a Public Method")
    def protected_method(self):
        print("Protected Variable")

obj1=Myclass()
obj2=Myclass()
print(obj1.public)
print(obj2._protected)
obj1.public_method()

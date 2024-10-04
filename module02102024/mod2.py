def greet(name):
    print("Hello",name)

class Person:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print("Intro:",self.name)

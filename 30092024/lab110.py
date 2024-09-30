class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def print_details(self):
        print("Your Details are:",self.__name,self.__age)

person=Person("Amit",34)
# Person.__name="Amit"
# person.__age=34
person.print_details()

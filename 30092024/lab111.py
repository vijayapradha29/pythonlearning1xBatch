#inorder to change the value of private variable use getter setter:
from tkinter.font import names


class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def print_details(self):
        print("Your Details are:",self.__name,self.__age)

person=Person("Amit",34)
# Person.__name="Amit"
# person.__age=34
person.print_details()
person.set_name("Dhivya")
name=person.get_name()
print(name)
person.print_details()
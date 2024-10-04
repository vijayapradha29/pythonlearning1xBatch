#collections:

from collections import namedtuple



Person=namedtuple("Person",["Name","Age","Gender"])
person=Person(Name="Vijaya",Age=23,Gender="Female")
print("Name",person.Name)
print("Age",person.Age)
print("Gender",person.Gender)


#instead of using nameedtuple we can use class as below:
class Person1:
    def __init__(self,Name,Age,Gender):
        self.Name=Name
        self.Age=Age
        self.Gender=Gender
    def print_details(self):
        print("Your Details are:",self.Name,self.Age,self.Gender)

person_object=Person1("Vijaya",23,"Female")
person_object.print_details()
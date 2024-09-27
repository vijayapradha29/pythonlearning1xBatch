#person with name,age,address attributes for 2 different objects

class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print("This is the First Line that will be printed")
    def print_details(self):
        print("My Details are:",self.name,self.age,self.address)

dhivya_object=Person("Dhivya",33,"abcd")
jagan_object=Person("Jagan",36,"efgh")

dhivya_object.print_details()
jagan_object.print_details()


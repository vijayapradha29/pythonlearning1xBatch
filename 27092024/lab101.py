#person
class Person:
    # name="Vijaya"
    def __init__(self,name):
        self.name=name
        print("Iam Creating the Object")
#or
    def Print_details(self):
        print("My Name is:",self.name)
    def print_details2(self):
        print("Your Name is:",self.name*2)

person1=Person("Vijaya")
person1.Print_details()
person1.print_details2()
person2=Person("Pradha")
person2.Print_details()
person2.print_details2()

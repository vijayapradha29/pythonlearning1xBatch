#create a class person and create 2 objects by taking input from users and print detaisl in the end.(name,age,address)

class Person:
    name=None
    age=None
    address=None
    def print_details_of_person1(self):
        print("The Details of  Person1 is:" + self.name, self.age, self.address)
    def print_details_of_person2(self):
        print("The Details of  Person2 is:"+ self.name,self.age,self.address)



person_name1=input("Enter person1 Name:\n")
person_name2=input("Enter person2 Name:\n")
person_age1=input("Enter person1 Age:\n")
person_age2=input("Enter person2 Age:\n")
person_address1=input("Enter person1 Address:\n")
person_address2=input("Enter person2 Address:\n")


person1_object=Person()
person1_object.name=person_name1
person1_object.age=person_age1
person1_object.address=person_address1
person1_object.print_details_of_person1()


person2_object=Person()
person2_object.name=person_name2
person2_object.age=person_age2
person2_object.address=person_address2
person2_object.print_details_of_person2()










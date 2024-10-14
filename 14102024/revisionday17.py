#class,objects:

class Person:
    name=None
    age=None
    phone_number=None
    height=None
    weight=None
    gender=None
    profession=None

    def run(self):
        print("Am Running")
    def sleep(self):
        print("Am Going to Sleep")
    def sing(self):
        print("I can Sing")
    def talk(self):
        print("I can Talk")
    def eat(self):
        print("I am going to eat")

person1=Person()
person1.name="Vijaya Pradha"
person1.age=23
person1.weight=66
person1.height=123.55
person1.gender="Female"
person1.profession="Housewife"
person1.phone_number=9875433322
person1.run()
print(person1.name)
print(person1)
person2=Person()
person2.name="Dhivya"
person2.age=33
person2.weight=67
person2.height=123.55
person2.gender="Female"
person2.profession="Housewife"
person2.phone_number=7568367567563
person2.sing()
print(person2.age)
print(person2)


class Cars:
    name=None
    model=None
    colour=None
    def print_car_details(self):
        print("My Car Details are:",self.name,self.model,self.colour)

figo=Cars()
car_name=input("Enter Car Name:\n")
car_model=input("Enter Car Model:\n")
car_colour=input("Enter Car Colour:\n")
figo.colour=car_colour
figo.model=car_model
figo.name=car_name
figo.print_car_details()


class Cars1:
    name=None
    model=None
    colour=None
    engine=None
    speed=None
    def break_type(self):
        print("Break")
    def clutch(self):
        print("Clutch")
    def start_engine(self):
        print("Engine Started")
    def stop_engine(self):
        print("Engine Stopped")
    def drive(self):
        print("Drive")
car_1=Cars1()
car_2=Cars1()
car_1.name="Figo"
car_2.name="Audi"
car_1.speed=150
car_2.speed=200
car_1.engine="Single Stroke"
car_2.engine="Double Stroke"
car_1.colour="Black"
car_2.colour="Dark Black"
car_1.model="I20"
car_2.model="I30"
car_1.start_engine()
car_2.stop_engine()
print(car_2.name)




class Person_new:
    name=None
    age=None
    address=None

    def print_detials_person1(self):
        print("The Details are:",self.name,self.age,self.address)
    def print_details_person2(self):
        print("The Details are:\n",self.name,self.age,self.address)

person_1=Person_new()
person_2=Person_new()

person_name1=input("Enter Your Name:\n")
person_name2=input("Enter Your Name:\n")
person_age1=int(input("Enter Your Age:\n"))
person_age2=int(input("Enter Your Age:\n"))
person_address1=input("Enter Your Address:\n")
person_address2=input("Enter Your Address:\n")

person_1.name=person_name1
person_2.name=person_name2
person_1.age=person_age1
person_2.age=person_age2
person_1.address=person_address1
person_2.address=person_address2


person_2.print_details_person2()

#class,objects:building

class Building:
    name=None
    id=None
    floor=None
    def buliding_details(self):
        print("The Building Details are:",self.name,self.id,self.floor)

building1=Building()
building_name1=input("Enter the Name of the building:\n")
building_id1=int(input("Enter the Building ID:\n"))
building_floor1=int(input("Enter the Floor:\n"))

building1.name=building_name1
building1.id=building_id1
building1.floor=building_floor1
building1.buliding_details()

#constructors:
#name,age,gender


class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def print_details(self):
        print("Your Details are:",self.name,self.age,self.gender)

dhivya=Person("Dhivya",23,"Female")
jagan=Person("Jagan",26,"Male")

dhivya.print_details()
jagan.print_details()

#encapsulation:
#public,Private,Protected:

class Cars:
    def __init__(self,name,model,colour):
        self.name=name
        self._model=model
        self.__colour=colour
    def print_car_details(self):
        print("Your Car Details are:",self.name,self._model,self.__colour)
car1=Cars("Figo","I20","Black")
car2=Cars("Toyota","Z20","Grey")
car1.print_car_details()
car2.print_car_details()
# print(car2._model)
# print(car1.__colour)


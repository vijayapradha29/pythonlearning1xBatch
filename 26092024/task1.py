#create a car class and create 2 objects of the class with attributes 5 and 5 methods

class Car:
    name=None
    model=None
    colour=None
    engine_type=None
    speed=None

    def break_type(self):
        print("Brake Type")
    def clutch(self):
        print("Clutch")
    def start_engine(self):
        print("Car Engine is Started")
    def Stop_engine(self):
        print("Car Engine is Stopped")
    def drive(self):
        return "Driving"


car_object=Car()
car_object.name="Tesla"
car_object.model="I10"
car_object.colour="Blue"
car_object.engine_type="Dual Engine"
car_object.speed=200

car1_object=Car()
car1_object.name="Lamborgini"
car1_object.model="Z20"
car1_object.colour="Black"
car1_object.engine_type="Single Engine"
car1_object.speed=150

car1_object.break_type()
car_object.start_engine()

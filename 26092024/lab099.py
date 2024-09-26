#get the input from the user and create a class,object

class Car:
    colour=None
    model=None
    def print_car_details(self):
        print("Your Car Details are:"+self.colour,self.model)

car_colour=input("Enter Your Car Colour:\n")
car_model=input("Enter Your Car Model:\n")

car_details=Car()
car_details.colour=car_colour
car_details.model=car_model
car_details.print_car_details()

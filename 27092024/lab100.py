#constructor:
#a=10->global variable,which is present outside the class
class Car:
    name="Vijaya"#class variable,which is present inside the class
    def __init__(self,make,model):
        self.make=make
        self.model=model
        print("I will be called First")
    def start(self):
        print("Starting a Car"+ self.make,self.model)
car1=Car("Toyota","Camry")
car2=Car("Honda","Civic")
print(id(car1))
print(id(car2))
car1.start()
car2.start()
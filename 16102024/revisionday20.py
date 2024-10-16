#polymorphism:
class Shape:
    def area(self):
        print("Area of Shape")
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
rect=Rectangle(3,2)
print(rect.area())
cir=Circle(3)
print(cir.area())
sha=Shape.area(2)

#overriding:

class Animal:
    def sound(self):
        print("Animal Sound")
class Dog(Animal):
    def sound(self):
        print("Dog Barks")

object=Dog()
object.sound()

#overloading:

class Mathutil:
    def add(self,a,b):
        print(a+b)
class Ad:
    def add(self,a,b,c):
        print(a+b+c)

ad=Mathutil()
ad.add(1,2)
ad1=Ad()
ad1.add(1,2,3)

#default values-overloading:

class Mathutil:
    def add(self,a,b=0,c=0):
        return a+b+c
math=Mathutil()
op1=math.add(1,2,3)
op2=math.add(1,2)
print(op1)
print(op2)

#abstraction:

from abc import ABC,abstractmethod

@abstractmethod
class Cars(ABC):
    def moveforward(self):
        pass
    def movebackward(self):
        pass
    def fm(self):
        pass
class Swift(Cars):
    def moveforward(self):
        print("Swift Car is moving Forward")
    def movebackward(self):
        print("Swift Car is moving Backward")
    def fm(self):
        print("Swift Car is having FM")
class Toyota(Cars):
    def moveforward(self):
        print("Toyota Car is moving Forward")
    def movebackward(self):
        print("Toyota Car is moving Backward")
    def fm(self):
        print("Toyota Car is having FM")
s=Swift()
s.movebackward()
t=Toyota()
t.moveforward()
c=Cars()
c.fm()


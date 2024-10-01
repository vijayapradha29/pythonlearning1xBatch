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

shape_rectangle=Rectangle(2,3)
print(shape_rectangle.area())
shape_circle=Circle(3)
print(shape_circle.area())
shape_shape=Shape()
shape_shape.area()
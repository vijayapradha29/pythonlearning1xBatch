#overloading:->traditional way is not possible in python

class Mathutil:
    def add(self,a,b):
        print(a+b)
class Mathutil1:
    def add(self,a,b,c):
        print(a+b+c)

math=Mathutil()
math.add(1,2)
math1=Mathutil1()
math1.add(1,2,3)
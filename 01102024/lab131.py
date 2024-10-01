#overloading:->traditional way is not possible in python

class Mathutil:
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c):
        print(a+b+c)

math=Mathutil()
math.add(1,2)
math.add(1,2,3)
#overloading is possible if we assign with default value

class Mathutil:
    def add(self,a,b=0,c=0):
        return a+b+c

math=Mathutil()
# op11=math.add()
# op11=math.add("Vijaya")
op0=math.add(1)
op1=math.add(1,2)
op2=math.add(1,2,3)
print(op0)
print(op1)
print(op2)
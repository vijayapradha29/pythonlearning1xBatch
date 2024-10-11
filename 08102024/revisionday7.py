#range:(start,stop,step)
#for loop:
from numpy.ma.core import equal, not_equal, nonzero

for i in range(1,10):
    print(i)
    result=list[i]
    print(result)

#while loop:
i=1
while i<=5:
    print(i)
    i+=1

#grade calculator:
mark=int(input("Enter Your Mark:\n"))
if mark>=90 and mark<=100:
    print("Grade A:",mark)
elif mark>=80 and mark<=89:
    print("Grade B:",mark)
elif mark>=70 and mark<=79:
    print("Grade C:",mark)
elif mark>=60 and mark<=69:
    print("Grade D:",mark)
elif mark>=40 and mark<=59:
    print("Grade F:",mark)
else:
    print("Invalid Input")

year=2029
zero=0
if year%4==0:
    if year%100 is nonzero:
        if year%400==0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")

#triangle classifier:
side1=int(input("Enter Side1:\n"))
side2=int(input("Enter Side2:\n"))
side3=int(input("Enter Side3:\n"))
if side1==side2==side3:
    print("Equilateral Triangle")
elif side1==side2 or side1==side3 or side2==side3:
    print("Isoceles Triangle")
elif side1!=side2!=side3:
    print("Scalene Triangle")
else:
    print("Enter Valid Input")
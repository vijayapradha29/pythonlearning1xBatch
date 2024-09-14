#Triangle Classifier
side1=int(input("Enter Side1:\n"))
side2=int(input("Enter Side2:\n"))
side3=int(input("Enter Side3:\n"))
if side1==side2==side3:
    print("It's a Equilateral Triangle")
elif side1==side2 or side1==side3:
    print("It's a Isoceles Triangle")
elif side1!=side2!=side3:
    print("It's a Scalene Triangle")
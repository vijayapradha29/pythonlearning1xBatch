#area of a circle:
radius=int(input("Enter the value of Radius:\n"))
pie=3.14
area=pie*(radius*radius)
print("The Area of a Circle is :",area)

num1=int(input("Enter First Number:\n"))
num2=int(input("Enter Second Number:\n"))
# print(type(num1))
result="num1 is less than num2" if num1<num2 else "num1 is equal to num2 " if num1==num2 else "num1 is greater than  num2"
print(result)

number1=int(input("Enter the First Number:\n"))
number2=int(input("Enter the Second Number:\n"))
number3=int(input("Enter the Third Number:\n"))
output="number1 is maximum" if (number1>number2 and number1>number3) else "number2 is maximum" if (number2>number1 and number2>number3) else "number3 is maximum" if (number3>number1 and number3>number2) else "all are equal"
print(output)

number=int(input("Enter the Number:\n"))
square=number*number
print(square)
cube=number**3
print(cube)


#if else condition:

#age>18 watch movie
# otherwise not

age=int(input("Enter Your Age:\n"))
if age<18:
    print("You are not allowed to watch movie")
else:
    print("You can watch movie")

#multiple if else condition:

x=10
y=10
if x<y:
    print("x is Less than y")
elif x>y:
    print("x is Greater than y")
else:
    print("x is Equal to y")
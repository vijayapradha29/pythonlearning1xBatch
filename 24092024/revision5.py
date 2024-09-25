# from selectors import SelectSelector
#
# pie=3.14
# r=3
# area_of_circle=pie*r*r
# print(area_of_circle)
#
# first_number=input("Enter the First Number:\n")
# second_number=input("Enter the Second Number:\n")
# first_number1=int(first_number)
# second_number1=int(second_number)
# result="first number is greater" if first_number1 >second_number1 else "less than" if first_number1<second_number1 else "Equal"
# print(result)
#
# number1=input(("Enter Number1:\n"))
# number2=input(("Enter Number2:\n"))
# number3=input(("Enter Number3:\n"))
# num1=int(number1)
# num2=int(number2)
# num3=int(number3)
# max="number1 is greater" if num1>num2 and num1>num3 else "number2 is greater" if num2>num1 and num2>num3 else "number3 is greater" if num3>num2 and num3>num1 else "enter numbers only"
# print(max)
#
# a=3
# square=a**2
# print(square)
# cube=a**3
# print(cube)
#
#
# #condition:
# #if...else
# #if this
# #else then
# #age>18->watch movie
# #age<18->cant watch movie
#
# age=input("Enter Your Age:\n")
# age1=int(age)
# if age1>=18:
#     print("You can Watch Movie")
# else:
#     print("You cannot Watch Movie")
#
# #multiple if else condition:
# x=10
# y=20
# if x>y:
#     print("X is Greater")
# elif x<y:
#     print("X is Lesser")
# else:
#     print("Equal")
#
# for i in range(1,10,2):
#     print(i)
#
# i=1
# while i<5:
#     print(i)
#     i=i+1

# mark=input("Enter Your Mark:\n")
# mark1=int(mark)
# if mark1>=90 and mark1<=100:
#     print("Grade A")
# elif mark1>=80 and mark1<=89:
#     print("Grade B")
# elif mark1>=70 and mark1<=79:
#     print("Grade C")
# elif mark1>=60 and mark1<=69:
#     print("Grade D")
# else:
#     print("Grade F")


# year=input("Enter the Year:\n")
# year1=int(year)
# if year1%4==0:
#     if year1%100==0:
#         if year1%400==0:
#             print("It's a Leap Year")
#         else:
#             print("It's not a Leap Year")
#     else:
#         print("It's a Leap Year")
# else:
#     print("It's not a Leap Year")

side1=input("Enter Side1:\n")
side2=input("Enter Side2:\n")
side3=input("Enter Side3:\n")
side11=int(side1)
side22=int(side2)
side33=int(side3)
if side11==side22==side33:
    print("Equilateral Triangle")
elif side11!=side22 and side11!=side33:
    print("Scalene Triangle")
elif side11==side22 or side11==side33:
    print("Isoceles Triangle")
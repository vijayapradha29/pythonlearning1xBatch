#find the maximum of three numbers
num1=int(input("Enter the First Number:\n"))
num2=int(input("Enter the Second Number:\n"))
num3=int(input("Enter the Third Number:\n"))
if num1>num2 and num1>num3:
    print("Num1 is Maximum")
elif num2>num1 and num2>num3:
    print("Num2 is Maximum")
else:
    print("Num3 is Maximum")
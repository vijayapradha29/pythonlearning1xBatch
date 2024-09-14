#use the ternary operator to find the maximum of 3 numbers entered by the user
num1 = int(input("Enter the First Number:\n"))
num2 = int(input("Enter the Second Number:\n"))
num3 = int(input("Enter the Third Number:\n"))
# result = "num1 is maximum" if(num1 > num2 and num1 > num3) else "num1 is mimimum" or "num2 is maximum" if(num2 > num3) else "num2 is minimum" or "num3 is maximum" if(num3 > num1 and num3 > num2) else "num3 is minimum"
# print(result)
result="num1 is maximum" if(num1>num2 and num1>num3) else "num2 is maximum" if(num2>num3 and num2>num1) else "num3 is maximum" if(num3>num1 and num3>num2) else "all are equal"
print(result)
#max_number=num1 if(num1>num2 and num1>num3) else (num2 if(num2>num3) else num3)
#print(f"The Maximum of {num1},{num2} and {num3} is:{max_number}")
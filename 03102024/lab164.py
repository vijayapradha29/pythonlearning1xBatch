#exception:
try:
    num1=int(input("Enter Num1:\n"))
    num2=int(input("Enter Num2:\n"))
    result=num1/num2
    print(f"Result:{result}")
except ValueError:
    print("Invalid Input")
except ZeroDivisionError:
    print("Either num1 is zero or num2 is zero")
# else:
#     print(f"Result:{result}")
finally:
    print("I will be always Executed")
#exceptions:

a=10
b=0
# print(a/b)

#handle:
#using try and except block

try:
    c=a/b
except Exception as Error:
    print(Error)

#exception:
try:
    x=int(input("Enter the Value of X:\n"))
    c=10/x
    print(c)
except Exception as Error:
    print("Error:",Error)
else:
    print("No Errors are Found")
finally:
    print("I will be Executed Always at the End")
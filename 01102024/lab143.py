#exceptions:
from logging import exception

a=int(input("Enter the Value of A:\n"))
b=int(input("Enter the Value of B:\n"))
try:
    c=a/b
    print(c)
except Exception as error:
    print(f"The value of {a} is divided by {b} so try to avoid the value as Zero,",error)
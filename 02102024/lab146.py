#exception-zerodivisionerror:

try:
    x=10/0
except ZeroDivisionError as error:
    print("Error:",error)

#2.
try:
    result=10/5
    print(result)
except ZeroDivisionError as error:
    print("Error:",error)
#exception-zerodivisionerror:

try:
    result=10/0
    print(result)
except ZeroDivisionError as error:
    print("Error:",error)
finally:
    print("I will be Executed any how!")
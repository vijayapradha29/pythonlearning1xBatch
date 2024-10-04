#exception:generalised way
try:
    x=10/0
    print(x)
except Exception as error:
    print("Error:",error)
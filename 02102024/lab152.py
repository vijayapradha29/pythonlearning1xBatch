#exception-Keyboard interrupt:click run button then on output console click on stop button you will get keyboard interrupt  exception.

try:
    x=int(input("Enter a Value:\n"))
    result=10/x
except ZeroDivisionError as error:
    print("Error:",error)
except ValueError as error:
    print("Error:",error)
else:
    print("There is no Exception.")
finally:
    print("I will be Executed anyhow!")
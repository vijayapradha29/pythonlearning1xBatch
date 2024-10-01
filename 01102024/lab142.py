#exceptions:
a=10
b=0
# print(a/b)

#how to handle exceptions:
#use try and except
try:
    c=a/b
except ZeroDivisionError as error:
    print(error)
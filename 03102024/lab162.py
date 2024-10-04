#exception:
#
# print("Insert the Card")
#
# a=10/0
#
# print("Remove the Card")

#how to handle it properly?
#use try,except block

print("Insert the Card")

try:
    a=10/0
except Exception as error:
    print("Error:",error)

print("Remove the Card")
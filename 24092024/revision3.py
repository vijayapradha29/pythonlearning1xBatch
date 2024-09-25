#strings:
#immutable
from os import cpu_count

name="Vijaya"
# name[0]="A"
# print(name)
name="Dhivya"
print(name)
#capitalize:
string="welcome"
cap=string.capitalize()
print(cap)
#id:
print(id(string))
#upper:
print(string.upper())
#lower:
print(string.lower())
#swapcase:
print(string.swapcase())
#title:
print(string.title())
#replace:
print(string.replace("welcome","hello"))
print(string.find("l"))
print(string.find("l",3,5))
print(string.count("l"))
new=None
print(type(new))
print(new)

user_input=None
user_input=123
print(user_input)
# None=123
# print(None)
my_lists=["abc",1,12.34,True]
print(my_lists)

del user_input
# print(user_input)
#\\
#\
#\n
#\t
#\b
print("hello world\\")
print("hello \"Welcome\" to my channel")
print("hello \n","welcome")
print("hello \t","welcome")
print("hello \b","welcome")
print("World")

print("Welcome %s" %"to my class")

list=[1,2,3,4,5,1,2,4]
print(list)

set={1,2,3,4,5,4,1,2}
print(set)

print('we all are,{}'.format('Equal'))
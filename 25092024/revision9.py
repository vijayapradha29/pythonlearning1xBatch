#list:
#merging list:
from abc import ABCMeta

list1=[1,2,3,4]
list2=['a','b',True,False,12.34,108.09]
merge_list=[list1,list2]
print(merge_list)

lists=[1,2,3,4]
if not lists:
    print("its not empty")
else:
    print("its empty")

#type conversion:
#str to int:
str1="121"
print(str1)
integer=int(str1)
print(integer)
#str to float:
str1=12.345
decimal=float(str1)
print(decimal)
#value to str:
value=True
string=str(value)
print(string)
#value to list:
string="Welcome"
new_list=list(string)
print(new_list)
#value to set:
string="hello"
sets=set(string)
print(sets)
#value to tuple:
string="how are you?"
new_tuple=tuple(string)
print(new_tuple)
#value to dictionary:
string={"name":"abc"}
new_dict=dict(string)
print(new_dict)
#value to boolean:
string="true"
boolean1=bool(string)
print(boolean1)
#bytes:
#complex number:

#to view functions of list:
a=dir(list)
print(a)

#map:
def square(a):
    return a**a
print(square(2))

output=lambda a:a**a
print(output(3))

numbers=[1,2,3,4,5]
output1=list(map(lambda a:a**a,numbers))
print(output1)


#set:
# set={}
from collections import namedtuple

set1={1,2,3,4,5}
set2=set(set1)
print(set2)
print(type(set1))
print(len(set1))
# print(set1[3])
# set1[3]="abc"
# print(set1)
set3={"abc",12.34,True,0,False,1}
print(set3)
list=[1,2,3]
print(set(list))
set11={12,13,15,20}
set12={11,12,13,14,15}
sets=set11.union(set12)
print(sets)
sets1=set11.difference(set12)
print(sets1)
sets2=set11.intersection(set12)
print(sets2)
sets3=set11.issubset(set12)
print(sets3)

#no arguments and no return:
# def hello():
#     print("Hi")
# a=hello()
# print(a)

#no argument but return:
def hi():
    return name
name="vijaya"
print(hi())

set20=["The Testing Academy","Welcome","Students"]
for i in set20:
    print(i)

set20.remove("Welcome")
print(set20)

list=[1,120,23,56,100]
list.sort()
print(list)
print("The Largest Number in the List is:",list[4])

print("The Smallest Number in the List is:",list[0])

list1=list[0]+list[1]+list[2]+list[3]+list[4]
print(list1)

list2=list[0]*list[1]*list[2]*list[3]*list[4]
print(list2)

new_list=["Vijaya",12,34,"name","Pradha",1,2,3,True,False,True,"Vijaya"]
print(new_list.count("Vijaya"))
#list:
my_list=[1,2,3,4,5,3,2]
#print lists:
print(my_list)
#length of list:
print(len(my_list))
#type:
print(type(my_list))
#access the value:
print(my_list[0])
#change the value:
my_list[0]="vijaya"
print(my_list)
my_list[2]=12.35
print(my_list)
my_list[4]=True
print(my_list)
#append:
my_list.append(False)
print(my_list)
#extend:
my_list.extend(["abc",3.12,False,True,90])
print(my_list)
#insert:
my_list.insert(3,"Hello")
print(my_list)
#remove:
my_list.remove(2)
print(my_list)
#copy:
copy1=my_list.copy()
print(copy1)
#clear:
copy1.clear()
print(copy1)
#sort:
my_list1=[3,1,10,8,5]
my_list1.sort()
print(my_list1)
#reverse:
my_list.reverse()
print(my_list)
#pop:
my_list.pop(2)
print(my_list)
print(my_list.remove(3.12))
list1=[1,2,3,4,5,6]
list2=list1
list3=list1.copy()
print(list1)
print(list2)
print(list3)
print(id(list1))
print(id(list2))
print(id(list3))
#slicing:
print(my_list[0:5])

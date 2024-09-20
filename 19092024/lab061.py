# #list
# my_lists=[1,2,3]
# #lists of integers
my_lists1=[1,True,"Vijaya",3.1444]
# print(my_lists1)
# print(my_lists1[0])
# #changing element in list:
# my_lists1[1]=30
# print("The element is been changed at index1 to:",my_lists1)
# #append:add element to the end of the list
# my_lists1.append("Welcome")
# print("The element added to the lists is:",my_lists1)
# #Extend:extend the lists by adding more than one element as a list
# my_lists1.extend([5,6,"Hello",False,2.87])
# print("List is Extended by:",my_lists1)
# #insert:
# my_lists1.insert(0,'abc')
# print("List after inserting 'abc' at index0 is:",my_lists1)
# #remove
# my_lists1.remove('abc')
# print("List after removing 'abc':",my_lists1)
# #copy:
my_copy_lists=my_lists1.copy()
print(my_copy_lists)
# #clear:
# my_lists.clear()
# print("Clear Lists:",my_lists)
# # print(my_copy_lists)
# # print(my_copy_lists[3])
# # print(my_lists[0])
# #sort:
my_copy_lists.sort()
print(my_copy_lists)
# my_copy_lists.reverse()
# print(my_copy_lists)
# print(my_copy_lists.remove(3.1444))
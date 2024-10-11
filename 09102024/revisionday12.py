
#
# list1=[1,2,3,4]
# list2=[5,6,7,8]
# new_list=[list1,list2]
# print(new_list)
# list=[]
# if not list:
#     print("empty")
# else:
#     print("not empty")
#
# list1.pop(2)
# print(list1)
#
# #map:
# #square:
# #map(function,iterable)
# def square(a):
#     return a*a
# print(square(2))
#
output=lambda a:a*a
print(output(2))
#
input_number=[1,2,3]
result=list(map(lambda a:a*a,input_number))
print(result)
#set:
from itertools import count

set11={}
set1=set({1,2,3,4})
print(set1)
print(len(set1))
print(type(set1))
new_set={1,2,3,1,2,4,5}
print(new_set)
# new_set[0]="abc"
# print(new_set)
diff_set={1,True,12.34,"abc"}
print(diff_set)

#largest:
list_new=[32,600,8000,100,200,504]
list_new.sort()
print(list_new[-1])
print(list_new[0])
sum_list=list_new[0]+list_new[1]+list_new[2]+list_new[3]+list_new[4]+list_new[5]
print(sum_list)
mul_list=list_new[0]*list_new[1]*list_new[2]*list_new[3]*list_new[4]*list_new[5]
print(mul_list)
string_list=["hello","madam","naman","hi"]
print(string_list.count("hello"))
#diff between pop() and popitem()
my_dict1={"a":"ABC","b":123,"C":True}
print(my_dict1.pop("b"))
print(my_dict1)
print(my_dict1.popitem())
print(my_dict1)
del my_dict1
# print(my_dict1)

#ordered dictionary:
from collections import OrderedDict
od=OrderedDict()
od["a"]=12
od["b"]=34
od["d"]=100
od["c"]=200
od["a"]=100
print(od)
#how to sort keys in ordered dictionary:
new_dict=dict(b=123,e="abc",i=True,d=12.34,k="DEF",z=123445,s=False)
# print(new_dict[0])
print(new_dict)
keys=list(new_dict.keys())
print(keys)
sort_keys=sorted(keys)
print(sort_keys)
rev_keys=list(reversed(sort_keys))
print(rev_keys)
new_dict1=list(new_dict.values())
print(new_dict1)
od1=OrderedDict()
od1[sort_keys[0]]=new_dict1[0]
print(od1)
od1[sort_keys[1]]=new_dict1[3]
od1[sort_keys[2]]=new_dict1[1]
od1[sort_keys[3]]=new_dict1[2]
od1[sort_keys[4]]=new_dict1[4]
od1[sort_keys[5]]=new_dict1[6]
od1[sort_keys[6]]=new_dict1[5]
print(od1)

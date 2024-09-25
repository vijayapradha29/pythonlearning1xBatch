#dictionary:
dict12={}
dictionary=dict(name="abc",age=12,isMarried=True)
print(len(dictionary))
print(type(dictionary))
dictionary["name"]="def"
print(dictionary)
print(dictionary["name"])
print(dictionary.get("name"))
print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())
# print(dictionary.keys(0))
convertion=list(dictionary)
print(convertion)
print(convertion[0])
#functions od dict:
print(dir(dict))
my_dict={"name":"abc","age":12,"isMarried":False}
for keys,val in my_dict.items():
    print(keys)
    print(val)
from collections import OrderedDict
od=OrderedDict()
od[0]="abc"
od[1]=123
od[2]=True
od[5]=1
od[4]=True
od[1]=134
print(od)
# print(od1)
list123=list(od)
print(list123)
sorting=sorted(list123)
print(sorting)


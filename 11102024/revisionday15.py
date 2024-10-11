#dictionary:
my_dict={}
my_dict1=dict()
print(type(my_dict))
print(type(my_dict1))
user_details={
    "name":"Vijaya",
    "age":23,
    "address":"jdgjkffkjhfj",
}
print(user_details)
print(len(user_details))
print(user_details["name"])

my_dict2=dict(vijaya=1234567,pradha=987655,dhivya=653285974)
print(my_dict2)
print(my_dict2['vijaya'])
print(my_dict2.get("pradha"))

my_dict3=dict(name="name",age=12,isMarried=True,pie=13.45)
print(my_dict3.get("isMarried"))
print(my_dict3.values())

my_dict4={'a':12,'b':13,'c':14,'d':15,'a':16,'d':17}
print(my_dict4.keys())
keys=list(my_dict4)
print(keys[0])
my_dict.clear()
print(my_dict)
my_dict5=my_dict4.copy()
print(my_dict5)
print(my_dict5.items())
pop_function=my_dict5.pop('a')
print(pop_function)
print(my_dict5)
print(dir(dict()))

for keys,values in my_dict5.items():
    print(keys,values)

my_dict6=dict(b=34,c=56,d=67,a=34,e=78,f=100)
print(my_dict6.popitem())
print(my_dict6)

from collections import OrderedDict

od=OrderedDict()
od['z']=45
od['c']=34
od['a']=54
od['e']=63
od['f']=74
od['b']=92
print(od)
sorted_keys=list(od.keys())
print(sorted_keys)
sorted_keys1=sorted(sorted_keys)
sorted_values=list(od.values())
print(sorted_values)
od2=OrderedDict()
od2[sorted_keys1[0]]=sorted_values[2]
od2[sorted_keys1[1]]=sorted_values[5]
od2[sorted_keys1[2]]=sorted_values[1]
od2[sorted_keys1[3]]=sorted_values[3]
od2[sorted_keys1[4]]=sorted_values[4]
od2[sorted_keys1[5]]=sorted_values[0]
print(od2)

my_dict7={'a':10,'b':11,'c':12,'d':13}
for keys,values in my_dict7.items():
    if values==11:
        print("Value is found in dictionary")
    # else:
    #     print("Value is not found in dictionary")

my_newdict={}
user_keys=input("Enter Key Name:\n")
value_keys=input("Enter Values:\n")
my_newdict[user_keys]=value_keys
print("Updated Dictionary:",my_newdict)
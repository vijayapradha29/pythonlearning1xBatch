my_dict={"a":1,"b":"dhfj","c":True,"d":23.344}
print(my_dict)
my_copy_dict=my_dict.copy()
print(my_copy_dict)

print(my_copy_dict.items())
set_dict=set(my_copy_dict.items())
print(set_dict)
# print(set_dict[0])

# pop:
my_dict={"a":123,"b":"Abc"}
# print(my_dict.pop("b"))
# print(my_dict)

print(dir(dict))
for keys,values in my_dict.items():
    print(keys)
    print(values)


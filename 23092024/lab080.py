new_dict=dict(name="Vijaya",age=23,isMarried=True,address="TN")
print(new_dict)
print(len(new_dict))
print(new_dict.get("age"))

dictionary={"name":"pramod",90:34,"isMarried":False,"Address":"TN"}
print(dictionary[90])
print(dictionary.values())

#no duplicates:
my_dict={"a":90,"b":48,"c":10,"a":10}
print(my_dict)
print(my_dict.keys())
# keys=my_dict.keys[0]
# print(keys)

keys=list(my_dict)
print(keys)
print(keys[0])
print(keys[1])
print(keys[2])

#clear:
my_dict.clear()
print(my_dict)

student_list={"name":"Vijaya","age":23,"RollNO":1234}
print(student_list)
student_list.clear()
print(student_list)
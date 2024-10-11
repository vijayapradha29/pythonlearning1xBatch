# palindrome using lambda:
input_string=input("Enter the String:\n")
def palindrome(input_string2):
    input_string1=input_string[::-1]
    return input_string1

output=palindrome(input_string)
print(output)
if input_string==output:
    print("palin")
else:
    print("Not Palin")

output=lambda input_string2:input_string[::-1]
output2=output(input_string)
print(output2)
if input_string==output2:
    print("Palin")
else:
    print("Not palin")

my_list=[1,2,3,4,"abc",True,23.87]
print(my_list)
print(type(my_list))
print(len(my_list))
print(my_list[0])
my_list[0]="hello"
print(my_list)
my_list[1]=True
print(my_list)
my_list.append(90)
print(my_list)
my_list.extend(["hi",False,90,34,67.90])
print(my_list)
my_list.insert(3,"welcome")
print(my_list)
my_list.remove(3)
print(my_list)
my_list1=my_list.copy()
print(my_list1)
my_list1.clear()
print(my_list1)
my_list.reverse()
print(my_list)
print(my_list.count(False))

#palindrome:
# user_input=input("Enter the Input:\n")

# def palindrome(user_input):
#     reverse_string=" "
#     for char in user_input:
#         reverse_string=char+reverse_string
#     return reverse_string
#
# original_string=input("Enter the Input:\n")
# rev_string=palindrome(original_string)
# print(rev_string)
# if original_string==rev_string:
#     print("Its a Palindrome")
# else:
#     print("Its not a Palindrome")
#
# #Lambda:
# #double:
# def double(a):
#     return a*a
# print(double(2))
#
# output=lambda a:a*a
# print(output(2))
#
# #name:
# def user_input(name):
#     print("Your Name is:",name)
#
# user_input("Vijaya")
#
# result=lambda name:print("Your Name is:",name)
# result("Vijaya")
#
# #right triangle pattern:
# number=int(input("Enter the Number:\n"))
# for i in range(1,number+1):
#     print("*"*i)

#count the vowels and consonants in a string:
# input1=input("Enter the String:\n")
# input2=input1.lower()
# con=len(input2)
# # print(con)
# # print(type(con))
# char=0
# space=0
# for i in input2:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#       char=char+1
#       vowels=char
# # print(char)
#     elif i==" ":
#         space=space+1
#         space1=space
# # print(space)
# consonants=con-vowels-space1
# # print(consonants)
# print("The Number of Vowels are:",vowels,"The Number of Consonants are:",consonants,"And the String contains:",space1,"Spaces")

#create function with x^y parameter:

def cap(x,y):
    return x**y
print(cap(2,3))

triple=lambda x:x**3
print(triple(2))
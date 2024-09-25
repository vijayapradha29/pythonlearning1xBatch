#lambda:
# def double(a):
#     return a*a
# print(double(2))
#
# double=lambda a:a*a
# print(double(2))
#
# def hello(name):
#     print("Welcome to Python Automation",name)
#
# hello("vijaya")
#
# output=lambda name:print("Welcome to Python Automation",name)
# output("vijaya")
#
# #triangle:
# n=5
# for i in range(1,n+1):
#  print("*"*i)
#
# #consonants and vowels:
# name=input("Enter your Name:\n")
# name1=len(name)
# character=0
# space=0
# for char in name:
#     if char=='a'or char=='e' or char=='i' or char=='o' or char=='u':
#         character=character+1
# # print(character)
# #     elif char==' ':
# #         space=space+1
# # # print(space)
# # total_characters=26
# # consonants=name1-character-space
# # print(consonants)
# #
# # print(f"The Number of Vowels is:{character} and the Number of Consonants is {consonants}")

#function:
def function(x,y):
    return x**y
print(function(2,3))

#lambda:
output=lambda x,y:x**y
print(output(2,3))
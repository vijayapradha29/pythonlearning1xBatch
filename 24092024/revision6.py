#break:
# n=1
# while n<=10:
#     print(n)
#     n=n+1
#     if n==5:
#         break
#
# #pass:
# for i in range(1,11):
#     if i==6:
#         pass
#     else:
#         print(i)
#
# #continue:
# for i in range(1,10):
#     if i==5:
#         print("its number 5")
#         continue
#     else:
#         print("done")
#
#fibonacci series:

# number=input("Enter the Number:\n")
# number1=int(number)
# a = 0
# b = 1
# while a<number1:
#     print(a,end="")
#     a,b=b,a+b

#factorial:
# number=5
# if number<0:
#     print("no factorial")
# # else:
# #     fact = 1
# #     for i in range(1, number + 1):
# #         fact=fact*i
# # print(fact)
#
# # for i in range(1,101):
# #     print(i)
# #     if i==51:
# #         break
# #     else:
# #         continue
#
# # #match:
# # days=input("Enter the day:\n")
# # match days:
# #     case "monday":
# #         print("Day Number1")
# #     case "tuesday":
# #         print("Day Number2")
# #     case "wednesday":
# #         print("Day Number3")
# #     case "thursday":
# #         print("Day Number4")
# #     case "friday":
# #         print("Day Number5")
# #
#
# #function:
# #with arguements and with return
# def sum(a,b):
#     return a+b
#
# output=sum(2,3)
# print(output)
#
# #no arguements and no return
#
# def hello():
#     print("Welcome")
#
# hello()
#
# #without arguements and with return:
#
# def sum():
#     return a+b
#
#
# a=int(input("Enter the value of a:\n"))
# b=int(input("Enter the value of b:\n"))
# # print(sum(a,b))
# print(a+b)
#
# #with arguements and no return:
# def hello(name):
#     print("Welcome to the testing academy",name)
#
# hello("Vijaya pradha")
#
#
# #palindrome checker:
#
# name=input("Enter any string:\n")
# name1=name[::-1]
# print(name1)
# if name==name1:
#     print("It's a Palindrome")
# else:
#     print("Not a Palindrome")
#
# def palindrome(input_String):
#     input_string1=input_String[::-1]
#     if input_String==input_string1:
#         print("It's a Palindrome")
#     else:
#         print("It's not a Palindrome")
#
# input_string=input("Enter any string:\n")
# palindrome(input_string)
#
# def palindrome(input_string):
#     rev_string = ""
#     for char in input_string:
#         rev_string = char + rev_string
#     if input_string==rev_string:
#         print("Palindrome")
#     else:
#         print("not a palindrome")
#
# input_string=input("Enter any String:\n")
# print(palindrome(input_string))
#
# def sum_of_integer(a,b,c):
#     return a+b+c
# print(sum_of_integer(1,2,3))
input_string=input("Enter the String:\n")
output=lambda input_string:input_string[::-1]
print(output(input_string))
if input_string==output(input_string):
    print("Palindrome")
else:
    print("not a Palindrome")

sum=lambda a,b,c:a+b+c
print(sum(1,2,3))

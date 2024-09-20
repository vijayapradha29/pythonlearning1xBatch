#palindrome:
# original_str="madam"
# def is_palindrome(original_str):
#     rev_str=original_str[::-1]
#     print(rev_str)
#     if rev_str==original_str:
#         print("It's a Palindrome")
#     else:
#         print("It's not a Palindrome")

original_str="madam"
rev_str=lambda original_str:original_str[::-1]
# print(rev_str)
if rev_str("madam")==original_str:
    print("It's a Palindrome")
else:
    print("Not a Palindrome")


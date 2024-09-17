#traditional and builtin function for palindrome program:

original_str="madam"
def is_palindrome(original_str):
    rev_str=original_str[::-1]
    print(rev_str)
    if rev_str==original_str:
        print("It's a Palindrome")
    else:
        print("It's not a Palindrome")

is_palindrome(original_str)
#or
#print(is_palindrome(original_str))
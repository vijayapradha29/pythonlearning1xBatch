original_str="ABCD"
def rev_string(original_str):
    rev_str=''.join(reversed(original_str))
    print(rev_str)
    if original_str==rev_str:
        print("It's a Palindrome")
    else:
        print("It's not a Palindrome")

rev_string(original_str)
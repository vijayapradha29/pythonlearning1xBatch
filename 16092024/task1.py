#Palindrome:
name=input("Enter the Name:\n")
name1=name[::-1]
print(name1)
if name1==name:
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")
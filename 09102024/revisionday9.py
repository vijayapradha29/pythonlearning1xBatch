#matchcase:
#days:
day=input("Enter the Day:\n")
match day:
    case "Monday":
        print("Its the First Day in a Week")
    case "Tuesday":
        print("Its the Second Day in a Week")
    case "Wednesday":
        print("Its the Third Day in a Week")
    case "Thursday":
        print("Its the Fourth Day in a Week")
    case "Friday":
        print("Its the Fifth Day in a Week")
    case "Saturday":
        print("Its the Sixth Day in a Week")
    case "Sunday":
        print("Its the Seventh Day in a Week")
    case _:
        print("Enter Valid Input")

#function:
#sum:
#function with arguements and return:

def sum(a,b):
    return a+b

print(sum(2,3))

#function with no arguements and no return:

def say_hello():
    print("Hi,Welcome to Revisionday 9")

say_hello()

#function with arguments and no return:

def user_name(name):
    print("Your Name is:",name)

user_name("Vijaya")

#palindrome checker:
#madam,madam
user_input=input("Enter Your Input Here:\n")
user_input1=user_input[::-1]
print(user_input1)
if user_input==user_input1:
    print("Its a Palindrome")
else:
    print("Its not a Palindrome")

#sum of the integers:

def sum(a,b,c,d):
    return a+b+c+d

print(sum(1,2,3,4))

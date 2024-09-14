#create a program that takes 2 numbers as input and prints whether the first number is greater than,less than or equal to the second number
first_number=input("Enter the First Number:\n")
second_number=input("Enter the Second Number:\n")
first_number=float(first_number)
second_number=float(second_number)
# print("First Number is greater" if first_number>= second_number else "Second Number is greater" or "First Number is lesser" if first_number<=second_number else "Second Number is lesser")
result="Greater Than" if first_number>second_number else "Less Than" if first_number<second_number else "Equal To"
print(f"{first_number} is {result} {second_number}")
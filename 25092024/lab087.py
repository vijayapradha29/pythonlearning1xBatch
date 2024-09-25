#retuen the numbers which are positive or greater than 0
numbers=[-1,10,3,-4,-6,-47,98]

def positive_numbers(numbers):
    return numbers>0
positive=list(filter(positive_numbers,numbers))
print(positive)
#tuple-filters:
numbers=[1,2,3,4,5,6,7,8,9,10]

def even_numbers(numbers):
    return numbers%2==0

output=tuple(filter(even_numbers,numbers))
print(output)
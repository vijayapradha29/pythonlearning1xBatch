# filter:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def new_filter(numbers):
    return numbers % 2 == 0


output=new_filter(2)
print(output)

#or
even_numbers=filter(new_filter,numbers)
print(even_numbers)
even_list=list(even_numbers)
print(even_list)

numlist = [30, 2, -15, 17, 9, 100]


# max_number_10=[30,17,100]

def max_number_10(numlist):
    return numlist > 10


output = max_number_10(numlist[0])
print(output)

output1 = lambda numlist: numlist > 10
print(output1(numlist[5]))
# or
output3 = list(filter(lambda numlist: numlist > 10, numlist))
print(output3)

output2 = list(filter(max_number_10, numlist))
print(output2)

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Smartphone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 100},
]
# print(type(products))
# print(type(products[0]))


# def affordable(products):
#     return products["price"] < 500
#
#
# output=affordable(products[3])
# print(output)

def affordable(products):
    return products["price"]<500
def affordable_name(products):
    return len(products["name"])<=6

output=list(filter(affordable,products))
print(output)
output1=list(filter(affordable_name,products))
print(output1)

for i in output:
    print(i["price"])
for i in output1:
    print(i["name"])

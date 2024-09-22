num=20

def multiply_by_10(n):
    n*=10
    num=n
    print("Value of num inside function:",num)
    return n
multiply_by_10(num)
print("Value of num outside function:",num)
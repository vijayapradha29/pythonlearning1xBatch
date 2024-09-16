#Grade Calculator:
mark=int(input("Enter Your Mark:\n"))
match mark:
    case match if match>=90:
        print("Your Grade is A")
    case match if match>=80:
        print("Your Grade is B")
    case match if match>=70:
        print("Your Grade is C")
    case match if match>=60:
        print("Your Grade is D")
    case _:
        print("Your Grade is F")



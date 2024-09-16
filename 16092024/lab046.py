#match:similar to switch case
number=int(input("Enter the Number:\n"))
match number:
    case 1:
        print("You have Entered1")
    case 2:
        print("You have Entered2")
    case _:
        print("No Idea")

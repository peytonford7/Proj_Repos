# String Menu

import sys

title = "menu".upper()
print(title.center(20, "="))
print("1. Coffee".ljust(16, ".") + "$1".rjust(4))
print("2. Muffin".ljust(16, ".") + "$2".rjust(4))
print("3. Cheesecake".ljust(16, ".") + "$4".rjust(4))

userinput = input("\n\nEnter an integer 1 - 3:\n\n")
choice = int(userinput)


match choice:
    case 1:
        print("You chose:")
        print("Coffee, $1\n\n")
    case 2:
        print("You chose:")
        print("Muffin, $2\n\n")
    case 3:
        print("You chose:")
        print("Cheesecake, $4\n\n")
    case _:
        sys.exit("You must enter an integer between 1-3.\n\n")
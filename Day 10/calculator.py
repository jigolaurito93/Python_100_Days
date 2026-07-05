logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a, b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

#Print Logo
print(logo)

def calculators():
    ask_for_first_num = True
    first_num = 0
    operator_dict = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }
    while True:
        if ask_for_first_num:
            #Ask for a number
            first_num = float(input("What's the first number?: ")) #if is_loop True
        #Ask for operation
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        #Ask for second number
        second_num = float(input("What's the next number?: "))
        result = operator_dict[operation](first_num, second_num)
        print(f"{str(first_num)} {operation} {str(second_num)} = {str(result)}")
        # Ask to continue calculation or start new calculation
        is_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.:\n").lower()
        if is_continue == "y":
            first_num = result
            ask_for_first_num = False
        elif is_continue == "n":
            ask_for_first_num = True
            
calculators()



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

def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def divide(num1, num2):
    return num1 / num2
def multiply(num1, num2):
    return num1 * num2

operation_dict = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
}

def calculator():
    is_accumulate = True
    print(logo)
    num1 = float(input("What's the first number?: "))
    while is_accumulate:
        for symbol in operation_dict:
            print(symbol)
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operation_dict[operation](num1, num2)
        #Display equation
        print(f"{num1} {operation} {num2} = {result}")
        # Ask to accumulate or restart from scratch
        is_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.:\n").lower()
        if is_continue == "y":
            num1 = result
        elif is_continue == "n":
            print("\n" * 20)
            calculator()

calculator()

from calculator_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def perform_calculation(n1, n2, operation_to_use):
    for operator in operations:
        if operator == operation_to_use:
            result = operations[operator](n1, n2)
    return result

def calculator():
    print(logo)
    n1 = float(input("Enter the first number: "))
    proceed = True
    while proceed:
        user_operation = input("What operation would you like to perform? (Choose +, -, *, /): ")
        n2 = float(input("Enter second number: "))
        result = perform_calculation(n1, n2, user_operation)
        print (f"{n1} {user_operation} {n2} = {result}\n")
        choice = input (f"Would you like to use {result} as the new 1st number? ('y' or 'n' or 'z' to exit): ").lower()
        print("*" *60)
        if choice == "y":
            n1 = result
            proceed = True
        elif choice == 'n':
            proceed = False
            print("\n" *20)
            calculator()
        else:
            exit()

calculator()
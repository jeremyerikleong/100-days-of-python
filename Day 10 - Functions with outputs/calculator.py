def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 * num2

math_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print("Welcome to Py-Calculator!")

should_accumulate = True
num1 = float(input("What is the first number?\n"))

while should_accumulate:
    for math_operation in math_operations:
        print(math_operation)
    operation_symbol = input("Let's choose an operation:\n")

    num2 = float(input("What is the second number?\n"))

    if operation_symbol in ("+", "-", "*", "/"):
        result = math_operations[operation_symbol](num1, num2)
        print(f"Solution: {num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue working with {result}, or type 'n' to reset the calculator\n").lower()

        if choice == "y":
            num1 = result
    else:
        print("Not a number, Math operation error! please enter a valid operation.")

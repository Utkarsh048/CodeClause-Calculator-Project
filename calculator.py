import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Error: Invalid input."

def power(x, y):
    return x ** y

def logarithm(x, base):
    if x > 0 and base > 0 and base != 1:
        return math.log(x, base)
    else:
        return "Error: Invalid input."

def display_menu():
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Exponentiation")
    print("7. Logarithm")
    print("8. Exit")

def calculator():
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("Exiting the calculator...")
            break

        if choice in ['1', '2', '3', '4', '6', '7']:
            num1 = float(input("Enter the first number: "))

        if choice in ['1', '2', '3', '4', '6', '7']:
            num2 = float(input("Enter the second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", square_root(num1))
        elif choice == '6':
            print("Result:", power(num1, num2))
        elif choice == '7':
            base = float(input("Enter the base: "))
            print("Result:", logarithm(num1, base))
        else:
            print("Invalid input. Please choose a number between 1 and 8.")

calculator()

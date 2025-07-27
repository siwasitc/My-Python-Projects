import os
import platform

from art import logo

# Basic math functions
def add(n1, n2):
    """Return the sum of n1 and n2"""
    return n1 + n2

# TODO: Write out the other 3 functions - subtract, multiply and divide.
def subtract(n1, n2):
    """Return the subtraction of n1 and n2"""
    return n1 - n2

def multiply(n1, n2):
    """Return the product of n1 and n2"""
    return n1 * n2

def divide(n1, n2):
    """Return the division of n1 and n2"""
    return n1 / n2

def get_non_zero_input(prompt):
    """Check to only receive non-zero input if the operation is division"""
    while True:
        try:
            value = float(input(prompt))
            if value != 0:
                return value
            print("❌ You can't divide by zero.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# TODO: Add these 4 functions into a dictionary as the values. Keys: "+", "-", "*", "/"
# Mapping operators to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# print(operations["*"](4,8))

# should_continue = True
def calculator():
    """
    A simple command-line calculator that allows users to perform basic arithmetic operations (_, -, *, /) repeatedly.
    :return:
    """
    while True:
        print(logo)

        # Initial input
        try:
            number_1 = float(input("What's the first number?: "))
        except ValueError:
            print("Please enter a valid number")
            continue

        # Starting the Loop for the calculation
        # user_continue = True
        while True:
            # Display available operators
            for operator in operations:
                print(operator)

            operation_choice = input("Pick an operation: ")
            if operation_choice not in operations:
                print("Invalid operation. Please choose one of the following: +, -, *, /")
                continue

            try:
                number_2 = float(input("What's the next number?: "))
            except ValueError:
                print("Please enter a valid number")
                continue

            if operation_choice == "/":
                # To manage division by zero
                number_2 = get_non_zero_input("Enter a non-zero number to divide by: ")
                result = operations[operation_choice](number_1, number_2)
            else:
                result = operations[operation_choice](number_1, number_2)

            # Show the result of the operation
            print(f"{number_1} {operation_choice} {number_2} = {result:.5f}")

            # Option to continue with result or restart
            user_choice = input(f"Type 'y' to continue calculating with {result:.5f}, or type 'n' to start a new calculation: ").lower()
            if user_choice == "y":
                number_1 = result
            else:
                # user_continue = False
                clear_screen()
                break
                # calculator()

calculator()
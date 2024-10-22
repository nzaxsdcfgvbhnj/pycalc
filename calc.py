#!/usr/bin/env python3

# -------------------------------------------------------- #
# -- CALCULATOR FUNCTIONS -------------------------------- #
# -------------------------------------------------------- #

# Add function
def add(a, b):
    return a + b

# Subtract function
def sub(a, b):
    return a - b

# Multiply function
def mult(a, b):
    return a * b

# Divide function
def div(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b


# -------------------------------------------------------- #

# -------------------------------------------------------- #
# -- MAIN FUNCTIONALITY ---------------------------------- #
# -------------------------------------------------------- #

a = None
b = None
op = None

while True:
    # get input values
    a = input("Enter the first argument: ")
    op = input("Enter the operation (+, -, *, /): ")
    b = input("Enter the second argument: ")
    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Invalid number argument...")
        op = None

    # decide function
    if op is not None:
        if op == "+":
            print("Sum: ", add(a, b))
        elif op == "-":
            print("Difference: ", sub(a, b))
        elif op == "*":
            print("Product: ", mult(a, b))
        elif op == "/":
            print("Quotient: ", div(a, b))
        else:
            print("Invalid operation...")

    q = input("Quit? [y/n] ")
    if q.lower() == "y":
        break

# -------------------------------------------------------- #

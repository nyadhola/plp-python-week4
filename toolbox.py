# Program: Toolbox
# Description: A collection of small helper functions.

def double(number):
    # Return the number multiplied by 2
    return number * 2

def is_pass(score):
    # Return True if score is 50 or more, otherwise False
    return score >= 50

def greet(name, greeting="Hello"):
    # Return the formatted greeting, name, and exclamation mark
    return f"{greeting}, {name}!"

# Tests
print(double(7))
print(double(10))
print(is_pass(80))
print(is_pass(20))
print(greet("Amina"))
print(greet("Brian", "Habari"))
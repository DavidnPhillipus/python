# Python Error Handling (Try/Except)
# Use try/except to handle errors without crashing the program.

try:
    value = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")

try:
    number = int("abc")
except ValueError:
    print("That is not a valid integer.")

# finally block
try:
    file = open("missing.txt", "r")
except FileNotFoundError:
    print("File not found.")
finally:
    print("This always runs.")

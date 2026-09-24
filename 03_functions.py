# Lesson 3: Functions

def greet(name):
    return f"Hello, {name}! Welcome to Python."


def add_numbers(a, b):
    return a + b


print(greet("David"))
print(add_numbers(10, 5))

# Default parameter

def describe_pet(name, animal="dog"):
    return f"{name} has a {animal}."


print(describe_pet("Max"))
print(describe_pet("Luna", "cat"))

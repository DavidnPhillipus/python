# Lesson 4: Lists, Tuples, Sets, and Dictionaries

# List
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print("Fruits:", fruits)

# Tuple
point = (10, 20)
print("Point:", point)

# Set
numbers = {1, 2, 3, 3, 4}
print("Unique numbers:", numbers)

# Dictionary
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

print("Student name:", student["name"])
print("Student course:", student.get("course"))

# List comprehension
squares = [n * n for n in range(1, 6)]
print("Squares:", squares)

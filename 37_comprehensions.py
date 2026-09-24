# Python Comprehensions
# Comprehensions provide a short way to create lists, sets, and dictionaries.

# List comprehension
squares = [x * x for x in range(1, 6)]
print(squares)

# Set comprehension
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print(even_numbers)

# Dictionary comprehension
student_grades = {"Alice": 90, "Bob": 85, "Charlie": 88}
passed = {name: grade for name, grade in student_grades.items() if grade >= 80}
print(passed)

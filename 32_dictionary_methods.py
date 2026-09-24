# Python Dictionary Methods
# Dictionaries store data in key-value pairs.

student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

print(student)

# keys()
print(student.keys())

# values()
print(student.values())

# items()
print(student.items())

# get()
print(student.get("name"))
print(student.get("city", "Unknown"))

# update()
student.update({"age": 21, "city": "Windhoek"})
print(student)

# pop()
student.pop("city")
print(student)

# copy()
new_student = student.copy()
print(new_student)

# clear()
new_student.clear()
print(new_student)

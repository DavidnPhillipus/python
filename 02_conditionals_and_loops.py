# Lesson 2: Conditionals and Loops

marks = 78

if marks >= 80:
    print("Excellent! You passed with distinction.")
elif marks >= 60:
    print("Good job! You passed.")
else:
    print("You need more practice.")

# For loop
for number in range(1, 6):
    print(f"Number: {number}")

# While loop
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1

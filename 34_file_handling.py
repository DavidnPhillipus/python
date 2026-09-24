# File Handling in Python
# Files are used to store data permanently.

# Writing to a file
file = open("example.txt", "w")
file.write("Hello from Python!\n")
file.write("This is a file lesson.\n")
file.close()

# Reading a file
file = open("example.txt", "r")
print(file.read())
file.close()

# Appending to a file
file = open("example.txt", "a")
file.write("Appending more text.\n")
file.close()

# Reading again
file = open("example.txt", "r")
print(file.read())
file.close()

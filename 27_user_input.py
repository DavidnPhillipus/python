print("Enter your name:") 
name = input() 
print(f"Hello {name}")

# Multiple Inputs 
# You can add as many inputs as you want, Python will stop executing at each of them, 
# waiting for user input: 
# Example 
# Multiple inputs: 
name = input("Enter your name:") 
print(f"Hello {name}") 
fav1 = input("What is your favorite animal:") 
fav2 = input("What is your favorite color:") 
fav3 = input("What is your favorite number:") 
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")
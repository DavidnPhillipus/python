Booleans represent one of two values: True or False. 

# Evaluate Values and Variables 
# The bool() function allows you to evaluate any value, and give you True or False in return, 
# Example 
# Evaluate a string and a number: 
print(bool("Hello")) 
print(bool(15))

# Functions can Return a Boolean 
# You can create functions that returns a Boolean Value: 
 
def myFunction() : 
 return True

if myFunction(): 
 print("YES!") 
else: 
 print("NO!") 

# Python also has many built-in functions that return a boolean value, like the isinstance() 
# function, which can be used to determine if an object is of a certain data type: 
# Example 
# Check if an object is an integer or not: 
x = 200 
print(isinstance(x, int))


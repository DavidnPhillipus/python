# If you create a variable with the same name inside a function, this variable will be local, 
# and can only be used inside the function. The global variable with the same name will 
# remain as it was, global and with the original value.

# To create a global variable inside a function, you can use the global keyword.
def myfunc(): 
global x 
x = "fantastic" 
myfunc() 
print("Python is " + x)



# To change the value of a global variable inside a function, refer to the variable by using the 
# global keyword:

x = "awesome" 
def myfunc(): 
global x 
x = "fantastic" 

myfunc() 
print("Python is " + x) 

# Setting the Data Type 
x = "Hello World", str,  
x = 20, int,  
x = 20.5, float,  
x = 1j, complex,  
x = ["apple", "banana", "cherry"], list,  
x = ("apple", "banana", "cherry"), tuple,  
x = range(6), range,  
x = {"name" : "John", "age" : 36}, dict,  
x = {"apple", "banana", "cherry"}, set,  
x = frozenset({"apple", "banana", "cherry"}), frozenset,  
x = True, bool,  
x = b"Hello", bytes,  
x = bytearray(5), bytearray,  
x = memoryview(bytes(5)), memoryview, 


# Setting the Specific Data Type  
x = str("Hello World"), str,  
x = int(20), int,  
x = float(20.5), float,  
x = complex(1j), complex,  
x = list(("apple", "banana", "cherry")), list,  
x = tuple(("apple", "banana", "cherry")), tuple,  
x = range(6), range, 

# Type Conversion
#convert from int to float: 
a = float(x) 
#convert from float to int: 
b = int(y) 
#convert from int to complex: 
c = complex(x)

# Random Number 
import random 
print(random.randrange(1, 10))


# Quotes Inside Quotes 
# You can use quotes inside a string, as long as they don't match the quotes surrounding the 
# string: 

print("It's alright") 
print("He is called 'Johnny'") 
print('He is called "Johnny"') 

# Multiline Strings 
# You can use three double quotes: 

a = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, 
sed do eiusmod tempor incididunt 
ut labore et dolore magna aliqua.""" 
print(a) 


# Strings are Arrays 
# Like many other popular programming languages, strings in Python are arrays of unicode 
# characters. 
# However, Python does not have a character data type, a single character is simply a string 
# with a length of 1. 
# Square brackets can be used to access elements of the string. 

# Get the character at position 1 (remember that the first character has the position 0): 
a = "Hello, World!" 
print(a[1]) 


# Looping Through a String 
# Since strings are arrays, we can loop through the characters in a string, with a for loop. 
 
for x in "banana": 
print(x) 



# String Length 
a = "Hello, World!" 
print(len(a)) 


# Check String 
# Check if "free" is present in the following text: 

# txt = "The best things in life are free!" 
# print("free" in txt) 


# Use it in an if statement: 
# Example 
# Print only if "free" is present: 

txt = "The best things in life are free!" 
if "free" in txt: 
print("Yes, 'free' is present.") 


# Check if "expensive" is NOT present in the following text: 
txt = "The best things in life are free!" 
print("expensive" not in txt) 



# Slicing 
# You can return a range of characters by using the slice syntax.

# Get the characters from position 2 to position 5 (not included): 
b = "Hello, World!" 
print(b[2:5]) 
 
# Slice From the Start  
b = "Hello, World!" 
print(b[:5]) 

# Slice To the End  
b = "Hello, World!" 
print(b[2:]) 

# Negative Indexing 
# Use negative indexes to start the slice from the end of the string:  
# From: "o" in "World!" (position -5) 
# To, but not included: "d" in "World!" (position -2): 
b = "Hello, World!" 
print(b[-5:-2])


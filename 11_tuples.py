# Python Tuples

mytuple = ("Govee", "OLED", "NVIDIA", "Sony")
# Whe creating a tuple with one Item you must add acomma at the end otherwise python will not recognise it as a tuple
thistuple = ("The Intelligent Investor",)

# A tuple can be of any ata type and you can even mix them in one tuple 
#  tuples are defined as objects with the data type 'tuple': 
# <class 'tuple'>

# The tuple() Constructor 
# It is also possible to use the tuple() constructor to make a tuple
thistuple = tuple(("apple", "banana", "cherry"))

# Python - Access Tuple Items 

# Access Tuple Items 
# You can access tuple items by referring to the index number, inside square brackets: 
rint(thistuple[1]) 


# Negative Indexing 
# Negative indexing means start from the end. 
print(thistuple[-1]) 

# Range of Indexes
# When specifying a range, the return value will be a new tuple with the specified items.
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) 

# Range of Negative Indexes 
# Specify negative indexes if you want to start the search from the end of the tuple: 
print(thistuple[-4:-1]) 

# Check if Item Exists
f "apple" in thistuple: 
    print("Yes, 'apple' is in the fruits tuple") 



# Change Tuple Values 
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or 
# immutable as it also is called. 
# But there is a workaround. You can convert the tuple into a list, change the list, and convert 
# the list back into a tuple. 


# Convert the tuple into a list to be able to change it: 
x = ("apple", "banana", "cherry") 
y = list(x) 
y[1] = "kiwi" 
x = tuple(y) 
print(x) 

# Add Items 
# Since tuples are immutable, they do not have a built-in append() method, but there are 
# other ways to add items to a tuple. 


# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a 
# list, add your item(s), and convert it back into a tuple. 
# Example 
# Convert the tuple into a list, add "orange", and convert it back into a tuple: 
thistuple = ("apple", "banana", "cherry") 
y = list(thistuple) 
y.append("orange") 
thistuple = tuple(y) 


# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one 
# item, (or many), create a new tuple with the item(s), and add it to the existing tuple: 
# Example 
# Create a new tuple with the value "orange", and add that tuple: 
thistuple = ("apple", "banana", "cherry") 
y = ("orange",) 
thistuple += y 
print(thistuple)


# Remove Items 

# Note: You cannot remove items in a tuple. 
# Tuples are unchangeable, so you cannot remove items from it, but you can use the same 
# workaround as we used for changing and adding tuple items: 

# Upacking tuples

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple: 

# Packing a tuple: 
fruits = ("apple", "banana", "cherry")

# Unpacking tuples 
( green, yellow, red ) = fruits

# Using the asterisc*
(green, *tropic, red) = fruits


# Loop Through a Tuple

for x in fruits:
    print(1)

# Loop Through the Index Numbers 
for i in range(len(thistuple)): 
print(thistuple[i]) 


x = 0
while x < len(thistuple):
    print(thistuple[x])
    x +=1

# Python - Join Tuples
# To join two or more tuples you can use the + operator: 
 
    # Join two tuples: 
    # tuple1 = ("a", "b" , "c") 
    # tuple2 = (1, 2, 3) 
    # tuple3 = tuple1 + tuple2 

# Multiply Tuples 
newFruits = fruits * 2
print(newFruits)


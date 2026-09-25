thisdict = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964,
"make": 1964,
} 

print(thisdict)

# to print the  length you have to use the len() funtion again
# The values in dictionary items can be of any data type: 
dict = { 
"brand": "Ford", 
"electric": False, 
"year": 1964, 
"colors": ["red", "white", "blue"] 
} 
# type()  
# <class 'dict'> 

# The dict() Constructor
isdict = dict(name = "John", age = 36, country = "Norway") 

# Python Collection Arrays
# Accessing Items 
# You can access the items of a dictionary by referring to its key name, inside square brackets:
x = thisdict["model"] 
p = thisdict.get("model")  #Here is another method that will give you the same result

# The keys() method will return a list of all the keys in the dictionary.
car = { 
"brand": "Ford", 
"model": "Mustang", 
"year": 1964 
} 
x = car.keys() 
print(x) #before the change 
car["color"] = "white" 
print(x) #after the change

# Get Values 
# The values() method will return a list of all the values in the dictionary.
o =  = thisdict.values() 

# Add a new item to the original dictionary, and see that the values list gets updated as well: 
car["color"] = "red" 
print(car)


# The items() method will return each item in a dictionary, as tuples in a list. 
# Example 
# Get a list of the key:value pairs 
x = thisdict.items() 

# Check if "model" is present in the dictionary: 
if "model" in thisdict: 
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Update the "year" of the car by using the update() method: 
thisdict.update({"year": 2020}) 

# The pop() method removes the item with the specified key name: 
thisdict.pop("model") 


# The popitem() method removes the last inserted item
thisdict.popitem()

# The del keyword removes the item with the specified key name:
del thisdict["model"] 

# The del keyword can also delete the dictionary completely: 
del thisdict 
print(thisdict) #this will cause an error because "thisdict" no longer exists.

# The clear() method empties the dictionary:
thisdict.clear() 


# Loop Through a Dictionary 
# You can loop through a dictionary by using a for loop.


# Print all key names in the dictionary, one by one: 
for x in thisdict: 
print(x) 

# You can also use the values() method to return values of a dictionary: 
for x in thisdict.values(): 
print(x)

# You can use the keys() method to return the keys of a dictionary: 
for x in thisdict.keys(): 
print(x)

# Loop through both keys and values, by using the items() method: 
for x, y in thisdict.items(): 
print(x, y) 

# Copy a Dictionary 
# Make a copy of a dictionary with the copy() method: 
mydict = thisdict.copy() 


# Another way to make a copy is to use the built-in function dict()
mydict = dict(thisdict)

# A dictionary can contain dictionaries, this is called nested dictionaries.

myfamily = { 
"child1" : { 
"name" : "Emil", 
"year" : 2004 
}, 
"child2" : { 
"name" : "Tobias", 
"year" : 2007 
}, 
"child3" : { 
"name" : "Linus", 
"year" : 2011 
} 
}

# Or, if you want to add three dictionaries into a new dictionary: 
myfamily = { 
"child1" : child1, 
"child2" : child2, 
"child3" : child3 
} 

# Access Items in Nested Dictionaries 
print(myfamily["child2"]["name"])

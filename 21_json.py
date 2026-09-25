# JSON in Python 
# Python has a built-in package called json, which can be used to work with JSON data.

import json 
# some JSON: 
x =  '{ "name":"John", "age":30, "city":"New York"}' 
# parse x: 
y = json.loads(x) 
# the result is a Python dictionary: 
print(y["age"])

# Convert from Python to JSON 
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method. 

# a Python object (dict): 
x = { 
"name": "John", 
"age": 30, 
"city": "New York" 
} 
# convert into JSON: 
y = json.dumps(x) 
# the result is a JSON string: 
print(y) 

# Format the Result 
# The example above prints a JSON string, but it is not very easy to read, with no indentations 
# and line breaks. 
# Use the indent parameter to define the numbers of indents: 
json.dumps(x, indent=4) 


# You can also define the separators, default value is (", ", ": "), which means using a comma 
# and a space to separate each object, and a colon and a space to separate keys from 
# values: 
# Example 
# Use the separators parameter to change the default separator: 
# json.dumps(x, indent=4, separators=(". ", " = ")) 


# Order the Result 
# The json.dumps() method has parameters to order the keys in the result: 
# Example 
# Use the sort_keys parameter to specify if the result should be sorted or not: 
# json.dumps(x, indent=4, sort_keys=True) 
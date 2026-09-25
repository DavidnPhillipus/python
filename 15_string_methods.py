# The upper() method returns the string in upper case: 
a = "Hello, World!" 
print(a.upper())

# The lower() method returns the string in lower case: 
a = "Hello, World!" 
print(a.lower())

# The strip() method removes any whitespace from the beginning or the end: 
a = " Hello, World! " 
print(a.strip()) # returns "Hello, World!" 

# Replace String 
# The replace() method replaces a string with another string: 
a = "Hello, World!" 
print(a.replace("H", "J"))

# Split String 
# The split() method returns a list where the text between the specified separator becomes 
# the list items. 
a = "Hello, World!" 
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation  
a = "Hello" 
b = "World" 
c = a + b 

# String Format 
# As we learned in the Python Variables chapter, we cannot combine strings and numbers 
# like this: 
 
age = 36 
#This will produce an error: 
txt = "My name is John, I am " + age 
print(txt) 

# But we can combine strings and numbers by using f-strings or the format() method! 
# F-Strings 
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings. 
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly 
# brackets {} as placeholders for variables and other operations. 

Example 
Create an f-string: 
age = 36 
txt = f"My name is John, I am {age}" 
print(txt)

# Placeholders and Modifiers 
# A placeholder can contain variables, operations, functions, and modifiers to format the 
# value. 
# Example 
# Add a placeholder for the price variable:

price = 59 
txt = f"The price is {price} dollars" 
print(txt) 


# A placeholder can include a modifier to format the value. 
# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which 
# means fixed point number with 2 decimals: 
# Example 
# Display the price with 2 decimals: 
price = 59 
txt = f"The price is {price:.2f} dollars" 
print(txt) 


# A placeholder can contain Python code, like math operations: 
# Example 
# Perform a math operation in the placeholder, and return the result: 
txt = f"The price is {20 * 59} dollars" 
print(txt)


# Escape Character 
# To insert characters that are illegal in a string, use an escape character. 
# An escape character is a backslash \ followed by the character you want to insert. 
# An example of an illegal character is a double quote inside a string that is 
# surrounded by double quotes:

# \' Single Quote  
# \\ Backslash  
# \n New Line  
# \r Carriage Return  
# \t Tab  
# \b Backspace  
# \f Form Feed


String Methods

capitalize() 
Converts the first character to upper case 

casefold() 
Converts string into lower case 

center() Returns a centered string 

count() Returns the number of times a specified value occurs in a string 

encode() 
Returns an encoded version of the string 

endswith() 
Returns true if the string ends with the specified value 

expandtabs() 
Sets the tab size of the string 

find() Searches the string for a specified value and returns the position of 
where it was found 

format() 
Formats specified values in a string

format_map() 
Formats specified values in a string 

index() Searches the string for a specified value and returns the position of 
where it was found 

isalnum() 
Returns True if all characters in the string are alphanumeric 
isalpha() 
Returns True if all characters in the string are in the alphabet 
isascii() Returns True if all characters in the string are ascii characters 
isdecim
 al() 
Returns True if all characters in the string are decimals 
isdigit() Returns True if all characters in the string are digits 
isidentif
 ier() 
Returns True if the string is an identifier 
islower(
 ) 
Returns True if all characters in the string are lower case 
isnumer
 ic() 
Returns True if all characters in the string are numeric 
isprinta
 ble() 
Returns True if all characters in the string are printable 
isspace
 () 
Returns True if all characters in the string are whitespaces 
istitle() Returns True if the string follows the rules of a title 
isupper
 () 
Returns True if all characters in the string are upper case 
join() Joins the elements of an iterable to the end of the string 
ljust() Returns a left justified version of the string 
lower() Converts a string into lower case 
lstrip() Returns a left trim version of the string 
maketr
 ans() 
Returns a translation table to be used in translations 
partitio
 n() 
Returns a tuple where the string is parted into three parts 
replace
 () 
Returns a string where a specified value is replaced with a specified 
value 
rfind() Searches the string for a specified value and returns the last position 
of where it was found 
rindex() Searches the string for a specified value and returns the last position 
of where it was found 
rjust() Returns a right justified version of the string 
rpartitio
 n() 
Returns a tuple where the string is parted into three parts 
rsplit() Splits the string at the specified separator, and returns a list 
rstrip() Returns a right trim version of the string 
split() Splits the string at the specified separator, and returns a list 
splitline
 s() 
Splits the string at line breaks and returns a list 
startswi
 th() 
Returns true if the string starts with the specified value 
strip() Returns a trimmed version of the string 
swapca
 se() 
Swaps cases, lower case becomes upper case and vice versa 
title() 
Converts the first character of each word to upper case 
translat
 e() 
Returns a translated string 
upper() 
Converts a string into upper case 
zfill() 
Fills the string with a specified number of 0 values at the beginning 
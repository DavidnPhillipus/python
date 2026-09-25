# Python RegEx 
# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. 
# RegEx can be used to check if a string contains the specified search pattern. 

import re 
txt = "The rain in Spain" 
x = re.search("^Thes.*Spaiin$", txt) 
print(x)

# RegEx Functions 
# The re module offers a set of functions that allows us to search a string for a match: 
# Function, Description 
# findall, Returns a list containing all matches 
# search, Returns a Match object if there is a match anywhere in the string 
# split, Returns a list where the string has been split at each match 
# sub, Replaces one or many matches with a string 


# Metacharacters 
# Metacharacters are characters with a special meaning: 
# Character, Description, Example, Try it 
# [], A set of characters, "[a-m]",  
# \, Signals a special sequence (can also be used to escape special characters), "\d",  
# ., Any character (except newline character), "he..o",  
# ^, Starts with, "^hello",  
# $, Ends with, "planet$",  
# *, Zero or more occurrences, "he.*o",  
# +, One or more occurrences, "he.+o",  
# ?, Zero or one occurrences, "he.?o",  
# {}, Exactly the specified number of occurrences, "he.{2}o",  
# |, Either or, "falls|stays",  
# (), Capture and group,  ,


# Flags 
# You can add flags to the pattern when using regular expressions. 
# Flag, Shorthand, Description, Try it 
# re.ASCII, re.A, Returns only ASCII matches,  
# re.DEBUG, , Returns debug information,  
# re.DOTALL, re.S, Makes the . character match all characters (including newline character),  
# re.IGNORECASE, re.I, Case-insensitive matching,  
# re.MULTILINE, re.M, Returns only matches at the beginning of each line,  
# re.NOFLAG, , Specifies that no flag is set for this pattern,  
# re.UNICODE, re.U, Returns Unicode matches. This is default from Python 3. For Python 2: 
# use this flag to return only Unicode matches,  
# re.VERBOSE, re.X, Allows whitespaces and comments inside patterns. Makes the pattern 
# more readable, 


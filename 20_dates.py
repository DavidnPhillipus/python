# Python Dates 
# A date in Python is not a data type of its own, but we can import a module named datetime 
# to work with dates as date objects. 

import datetime 
x = datetime.datetime.now() 
print(x) 

# Creating Date Objects 
# To create a date, we can use the datetime() class (constructor) of the datetime module.

u = datetime.datetime(2020, 5, 17) 
print(u)

# The strftime() Method 
# The method is called strftime(), and takes one parameter, format, to specify the format of 
# the returned string:

x = datetime.datetime(2018, 6, 1) 
print(x.strftime("%B"))

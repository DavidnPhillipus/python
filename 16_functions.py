# Python Functions
def my_function(): 
    print("Hello from a function") 

my_function()

# Arguments 

def my_function(fname): 
    print(fname + " Refsnes") 
my_function("Emil") 
my_function("Tobias") 
my_function("Linus") 

# Arbitrary Arguments, *args 
# If you do not know how many arguments that will be passed into your function, add a * 
# before the parameter name in the function definition. 
# This way the function will receive a tuple of arguments, and can access the items 
# accordingly: 

def my_function(*kids): 
    print("The youngest child is " + kids[2]) 
my_function("Emil", "Tobias", "Linus") 




# Keyword Arguments 
# You can also send arguments with the key = value syntax. 
# This way the order of the arguments does not matter. 
 
def my_function(child3, child2, child1): 
    print("The youngest child is " + child3) 
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 

# Arbitrary Keyword Arguments, **kwargs 
# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition. 
# This way the function will receive a dictionary of arguments, and can access the items 
# accordingly: 
 
# If the number of keyword arguments is unknown, add a double ** before the parameter name: 
def my_function(**kid): 
    print("His last name is " + kid["lname"]) 
my_function(fname = "Tobias", lname = "Refsnes") 

# Default Parameter Value 
def my_function(country = "Norway"):
    print("I am from " + country) 

my_function("Sweden") 
my_function("India") 
my_function() 

# Passing a List as an Argument 
# You can send any data types of argument to a function (string, number, list, dictionary 
# etc.), and it will be treated as the same data type inside the function.

# Return Values 
# To let a function return a value, use the return statement: 

def my_function(x): 
return 5 * x 
print(my_function(3))


# The pass Statement 
# function definitions cannot be empty, but if you for some reason have a function definition 
# with no content, put in the pass statement to avoid getting an error. 

def myfunction(): 
    pass

 

#  Positional-Only Arguments 
 
# Without the , / you are actually allowed to use keyword arguments even if the function 
# expects positional arguments: 
def my_function(x): 
    print(x) 
my_function(x = 3)


# Keyword-Only Arguments 
# To specify that a function can have only keyword arguments, add *, before the arguments: 
# Example 
def my_function(*, x): 
print(x) 
my_function(x = 3) 
 
#  Combine Positional-Only and Keyword-Only 
# You can combine the two argument types in the same function. 
# Any argument before the / , are positional-only, and any argument after the *, are keyword only. 

def my_function(a, b, /, *, c, d): 
    print(a + b + c + d) 
my_function(5, 6, c = 7, d = 8)


Python Lambda 
# A lambda function is a small anonymous function. 
# A lambda function can take any number of arguments, but can only have one expression. 

# lambda arguments : expression 
# The expression is executed and the result is returned: 
# ExampleGet your own Python Server 
# Add 10 to argument a, and return the result: 
x = lambda a : a + 10 
print(x(5)) 

# Lambda functions can take any number of arguments:  
# Multiply argument a with argument b and return the result: 
x = lambda a, b : a * b 
print(x(5, 6))

# Summarize argument a, b, and c and return the result: 
x = lambda a, b, c : a + b + c 
print(x(5, 6, 2)) 


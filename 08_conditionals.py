If statement: 
a = 33 
b = 200 
if b > a: 
print("b is greater than a") 

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition". 

if b > a: 
    print("b is greater than a") 
elif a == b:
    print("a and b are equal") 


# The else keyword catches anything which isn't caught by the preceding conditions. 

if b > a: 
    print("b is greater than a") 
elif a == b: 
    print("a and b are equal") 
else: 
    print("a is greater than b")

# Short Hand If
if a > b: print("a is greater than b") 
print("A") if a > b else print("B") 

# The and keyword is a logical operator, and is used to combine conditional statements: 
if a > b and c > a: 

# The or keyword is a logical operator, and is used to combine conditional statements:
if a > b or a > c: 
    print("At least one of the conditions is True")

# The not keyword is a logical operator, and is used to reverse the result of the conditional statement:
if not a > b: 
    print("a is NOT greater than b") 

# You can have if statements inside if statements, this is called nested if statements. 
 
x = 41 
if x > 10: 
    print("Above ten,") 
if x > 20: 
    print("and also above 20!") 
else: 
    print("but not above 20.")

# The pass Statement 
# if statements cannot be empty, but if you for some reason have an if statement with no 
# content, put in the pass statement to avoid getting an error. 

a = 33 
b = 200 
if b > a: 
    pass

# The Python Match Statement 
# Instead of writing many if..else statements, you can use the match statement. 
# The match statement selects one of many code blocks to be executed. 
# SyntaxGet your own Python Server 

match expression: 
case x: 
    code block 
case y: 
    code block 
case z: 
    code block 

day = 4 
match day: 
case 1: 
    print("Monday") 
case 2: 
    print("Tuesday") 
case 3: 
    print("Wednesday") 
case 4: 
    print("Thursday") 
case 5: 
    print("Friday") 
case 6: 
    print("Saturday") 
case 7: 
    print("Sunday") 


# Default Value 
# Use the underscore character _ as the last case value if you want a code block to execute 
# when there are not other matches: 

day = 44 
match day: 
case 6: 
print("Today is Saturday") 
case 7: 
print("Today is Sunday") 
case _: 
print("Looking forward to the Weekend") 


# Combine Values 
# Use the pipe character | as an or operator in the case evaluation to check for more than 
# one value match in one case: 
# Example 
day = 4 
match day: 
case 1 | 2 | 3 | 4 | 5: 
print("Today is a weekday") 
case 6 | 7: 
print("I love weekends!")

# If Statements as Guards 
# You can add if statements in the case evaluation as an extra condition-check: 

month = 5 
day = 4 
match day: 
case 1 | 2 | 3 | 4 | 5 if month == 4: 
    print("A weekday in April") 
case 1 | 2 | 3 | 4 | 5 if month == 5: 
    print("A weekday in May") 
case _: 
    print("No match")


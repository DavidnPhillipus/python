# The while Loop 
# With the while loop we can execute a set of statements as long as a condition is true. 
 
i = 1 
while i < 6: 
print(i) 
i += 1 


# The break Statement 
# With the break statement we can stop the loop even if the while condition is true: 

i = 1 
while i < 6: 
print(i) 
if i == 3: 
break 
i += 1 


# The continue Statement 
# With the continue statement we can stop the current iteration, and continue with the next: 
 
i = 0 
while i < 6: 
i += 1 
if i == 3: 
continue 
print(i) 


# The else Statement 
# With the else statement we can run a block of code once when the condition no longer is true: 

# Print a message once the condition is false: 
i = 1 
while i < 6: 
    print(i) 
    i += 1 
else: 
    print("i is no longer less than 6")


# Python For Loops 
#fruits = ["apple", "banana", "cherry"] 
for x in fruits: 
print(x) 

# The same goes when you are doing the same for strings
# You can also use the break and the continue keyword

# Using the range() function: 
for x in range(6): 
    print(x) 

for x in range(2, 6): 
    print(x) 
# note 6 is exclusive

# Increment the sequence with 3 (default is 1): 
for x in range(2, 30, 3): 
    print(x)

# Else in For Loop 
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished: 

# Print all numbers from 0 to 5, and print a message when the loop has ended: 
for x in range(6): 
    print(x) 
else: 
    print("Finally finished!")  

# Nested Loops 
for x in adj: 
    for y in fruits: 
        print(x, y)


# The pass Statement 
# for loops cannot be empty, but if you for some reason have a for loop with no content, put 
# in the pass statement to avoid getting an error.  

for x in [0, 1, 2]: 
  pass 



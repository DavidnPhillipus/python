# What are Classes and Objects? 
    # A class defines what an object should look like, and an object is created based on that 
    # class.

class MyClass: 
    x = 5 

# Create Object 
# Create an object named p1, and print the value of x: 
p1 = MyClass() 
print(p1.x)


# The __init__() Method 
# Create a class named Person, use the __init__() method to assign values for name and age: 
class Person0: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
p10 = Person0("John", 36)


# The __str__() Method 
# The __str__() method controls what should be returned when the class object is 
# represented as a string. 
# Without this method u would only print the objects location in memory but with it present you can actualy orint them values
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
p1 = Person("John", 36) 
print(p1) 

class Person2:
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def __str__(self): 
        return f"{self.name}({self.age})" 
    
p2 = Person2("David" , 20)
print(p2)


# Create Methods 
# You can create your own methods inside objects. Methods in objects are functions that 
# belong to the object.


class Person5: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def myfunc(self): 
        print("Hello my name is " + self.name) 
p1 = Person("John", 36) 
p1.myfunc() 

# Note: The self parameter is a reference to the current instance of the class, and is used to 
# access variables that belong to the class. 

# Modify Object Properties 
# You can modify properties on objects like this: 
# Set the age of p1 to 40: 
p1.age = 40 

# Delete Object Properties 
# You can delete properties on objects by using the del keyword: 
# Delete the age property from the p1 object: 
del p1.age

# You could alse delete the whole object this way
del p1 

# The pass Statement 
# class definitions cannot be empty, but if you for some reason have a class definition with 
# no content, put in the pass statement to avoid getting an error. 

class Person6: 
    pass


# Create an Iterator 
# To create an object/class as an iterator you have to implement the methods __iter__() and 
# __next__() to your object. 

class MyNumbers: 
    def __iter__(self): 
        self.a = 1 
        return self 
    def __next__(self): 
        x = self.a 
        self.a += 1 
        return x 
myclass = MyNumbers() 
myiter = iter(myclass) 
print(next(myiter))
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter)) 
print(next(myiter))

# StopIteration
# The example above would continue forever if you had enough next() statements, or if it was 
# used in a for loop. 
# To prevent the iteration from going on forever, we can use the StopIteration statement. 
# In the __next__() method, we can add a terminating condition to raise an error if the 
# iteration is done a specified number of times: 

def __next__(self): 
    if self.a <= 20: 
        x = self.a 
        self.a += 1 
        return x 
    else: 
        raise StopIteration 
myList = [ "apple", "banana", "cherry"]
thisIsMyList = ["Gaming" , "Intreprenuership", "coding", "AI and machine learning" , "Reading nice books"]
print(thisIsMyList)


#This Lists can conntain items of one data type or one for mixed data types
#And just like we haw mentioned before we can find the lists length by passing the variable in the len() function

thisList = list(("Javascript", "Python" , "React" , "Tailwind CSS" , "HTML and CSS" , "Node", "Express" , "PstgeSQL"))

# Accessing List Items
# Lists can be accessed by using their indexes just like in Javascript

# Negative simply means to start from the end of the list and the end is not negative Zero but negavaive one 
print(thisList[-2])

# Range of indexes formmore explamations visit the note mate

print(thisIsMyList[2:4])

# Check if item exists


if "Java" in thisList:
    print("What the fuck are you going to use that old language for")
else:
    print("Congrats mate Java is a pain in the butt")

# Change the item value

newList = ["Zero To One" , "Atomic Habits" , "Personal MBA"]

newList[1] = "5 Am Club"
print(newList)

# Change a range of items

lst = [ "ballerina" , "java" , "HTML And Css" , "Python"]
lst[ :1] = ["Node.js", "JavaScript"]

#If you insert more than you replaced the new items will be inserted where you specified and the remaining ones will move accordingly

# Insert Items
lst.insert(2 , "Express.js")


# Add Items to the list 

lst.append("HTML And Css")

#Extend List
additional = ["Next.js", "MongoDB" , "Prisma"] 

lst.extend(additional)
# Note that you can append any iterable datatype to anothe using the extend keyword it doesn't just apply to the Lists for some reason


#Removing From a List
# Removing a specific Item 

lst.remove("HTML And Css")

# Removing specific index
lst.pop()

# Remove specified index

del lst(4)

# Clear the List 

# lst.clear()


# Pthon Loop Lists

for x in thisIsMyList:
    print(x)

# Loop Through the Indes Numbers
# Use the range() and the len()functions to create asuitable iterable 

for i in range(len(thisList)):
    print(thisList[])

# Usong a while loop

i = 0
while i < len(lst):
    ptint(lst)
    i +=1

# Loooping using List Comprehnsion
# A shprt hande for loop that will print all items in a list:


[print(x) for x in thisIsMyList]

# List Comprehnsion
newLst = [x for x in thisList if "a" in x ]
print(newLst)

# This can be for all the iterable object 
#  You can use range to to create a new iterabe object

newIterable = [x for x in range(10)]


# THE EXPRESSION - this is the current item ib the iteration, but it is also the out come, which you can manupulate befor it endes up like a list item in the new list

new = [ x.upper() for x in thisIsMyList ]
new2 = [ "hello" for x in thisIsMyList]
new3 = [ if x != "Ptthon" else "GoLang" for x in thisIsMyList]

# Sorting the  Lists Alphanumerically
# The sort() will always sort list alphanumerically asc by default

thisList.sort()
print(thisList)

# Sort the list numeriacally
nums = [ 100 , 39 , 50  , 1 ]
nums.sort()
print(nums)

# Sort desc
nums.sort( reverse = True )
new2.sort( reverse = True )


# Customixe the Sort Function

# You can also customize your own function by using the keyword argument key = function. 
# The function will return a number that will be used to sort the list (the lowest number first): 
# Example

# Sort the list based on how close the number is to 50:

def myfunc(n): 
return abs(n - 50) 
thislist = [100, 50, 65, 82, 23] 
thislist.sort(key = myfunc) 
print(thislist) 

# Case Insensitive Sort 
# By default the sort() method is case sensitive, resulting in all capital letters being sorted 
# before lower case letters: 
# Example 
# Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"] 
thislist.sort() 
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list. 
# So if you want a case-insensitive sort function, use str.lower as a key function: 
# Example 
# Perform a case-insensitive sort of the list: 
thislist = ["banana", "Orange", "Kiwi", "cherry"] 
thislist.sort(key = str.lower) 
print(thislist) 


# Reverse Order 
# What if you want to reverse the order of a list, regardless of the alphabet? 
# The reverse() method reverses the current sorting order of the elements. 
# Example 
# Reverse the order of the list items: 

thislist = ["banana", "Orange", "Kiwi", "cherry"] 
thislist.reverse() 
print(thislist)



# Python - Copy Lists 
# You can use the built-in List method copy() to copy a list. 

thislist = ["apple", "banana", "cherry"] 
mylist = thislist.copy() 
print(mylist)

# Use the list() method
mylist = list(thislist) 
print(mylist)

# Use the slice Operator 
mylist = thislist[:] 
print(mylist)



# Python - Join Lists 
# Join Two Lists 
# There are several ways to join, or concatenate, two or more lists in Python. 
# One of the easiest ways are by using the + operator.


list1 = ["a", "b", "c"] 
list2 = [1, 2, 3] 
list3 = list1 + list2 
print(list3) 


# Another way to join two lists is by appending all the items from list2 into list1, one by one: 
for x in list1:
    list1.append(x) 

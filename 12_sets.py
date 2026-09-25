# Create a Set: 
thisset = {"apple", "banana", "cherry"} 
print(thisset) 

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates: 
# False and 0 is considered the same value: 
# To determine how many items a set has, use the len() function.

# Get the number of items in a set: 
print(len(thisset)) 

# Sets can be of any types and can contain a mixture of types too
# <class 'set'>

# The set() Constructor 
# thisset = set(("apple", "banana", "cherry")) # note the double round-brackets 
print(thisset) 

# Python - Access Set Items
# You cannot access items in a set by referring to an index or a key.
 

for x in thisset: 
  print(x)

# Change Items 
# Once a set is created, you cannot change its items, but you can add new items.


# Python - Add Set Items
# To add one item to a set use the add() method.
thisset.add("orange") 

# To add items from another set into the current set, use the update() method. 


thisset1 = {"apple", "banana", "cherry"} 
tropical = {"pineapple", "mango", "papaya"} 
thisset.update(tropical) 
print(thisset1)

# The object in the update() method does not have to be a set, it can be any iterable object 
# (tuples, lists, dictionaries etc.).

# Python - Remove Set Items 

# To remove an item in a set, use the remove(), or the discard() method. 
thisset.remove("banana") 

# Note: If the item to remove does not exist, remove() will raise an error.
# Note: If the item to remove does not exist, discard() will NOT raise an error. 
# You can also use the pop() method to remove an item, but this method will remove a 
# random item, so you cannot be sure what item that gets removed. 
# The return value of the pop() method is the removed item.

# The clear() method empties the set: 

# Python - Loop Sets 
for x in thisset: 
  print(x) 

# Python - Join Sets 


# There are several ways to join two or more sets in Python. 


# Union 
# The union() method returns a new set with all items from both sets. 
set1 = {"a", "b", "c"} 
set2 = {1, 2, 3} 
set3 = set1.union(set2) 

# You can use the | operator instead of the union() method, and you will get the same result.
set4 = set1 | set2


# Join a Set and a Tuple 
# The union() method allows you to join a set with other data types, like lists or tuples. 
z = x.union(y) 

# Note: The  | operator only allows you to join sets with sets, and not with other data types 
# like you can with the  union() method.

 
# The update() method inserts all items from one set into another. 
# The update() changes the original set, and does not return a new set.
# Note: Both union() and update() will exclude any duplicate items. 


# Intersection 
# Keep ONLY the duplicates 
# The intersection() method will return a new set, that only contains the items that are present in both sets. 

# Join set1 and set2, but keep only the duplicates: 
set0 = {"apple", "banana", "cherry"} 
set9 = {"google", "microsoft", "apple"} 
set8 = set1.intersection(set2) 
print(set3) 

# You can use the & operator instead of the intersection() method, and you will get the same result.
set3 = set1 & set2

# The intersection_update() method will also keep ONLY the duplicates, but it will change 
# the original set instead of returning a new set.
set1.intersection_update(set2) 


# Difference 
# The difference() method will return a new set that will contain only the items from the first 
# set that are not present in the other set.
 set3 = set1.difference(set2) 

# You an use the - operator instead of the difference() method, and you will get the same 
# result.
set3 = set1 - set2 

# Use the difference_update() method to keep the items that are not present in both sets: 
set1.difference_update(set2) 
print(set1)


# Symmetric Differences 
# The symmetric_difference() method will keep only the elements that are NOT present in 
# both sets. 
set13 = set1.symmetric_difference(set2) 
print(set13) 

# You can use the ^ operator instead of the symmetric_difference() method, and you will get 
# the same result. 
set03 = set1 ^ set2 
print(set03)

# Note: The ^ operator only allows you to join sets with sets, and not with other data types 
# like you can with the symmetric_difference() method. 


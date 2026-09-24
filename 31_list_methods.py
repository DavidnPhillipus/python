# Python List Methods
# Lists are used to store multiple items in a single variable.

fruits = ["apple", "banana", "cherry"]
print(fruits)

# append()
fruits.append("orange")
print(fruits)

# insert()
fruits.insert(1, "mango")
print(fruits)

# remove()
fruits.remove("banana")
print(fruits)

# pop()
last_item = fruits.pop()
print(last_item)
print(fruits)

# sort()
numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)

# reverse()
numbers.reverse()
print(numbers)

# copy()
copy_list = numbers.copy()
print(copy_list)

# clear()
copy_list.clear()
print(copy_list)

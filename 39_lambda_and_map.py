# Python Lambda and Map
# Lambda functions are small anonymous functions.

add_ten = lambda x: x + 10
print(add_ten(5))

numbers = [1, 2, 3, 4, 5]

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Filter example
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(filtered)

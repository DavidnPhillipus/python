# Python Sets and Frozensets
# A set is a collection of unique items.

numbers = {1, 2, 3, 4, 4, 5}
print(numbers)

# add()
numbers.add(6)
print(numbers)

# remove()
numbers.remove(2)
print(numbers)

# union()
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a | set_b)

# intersection()
print(set_a & set_b)

# difference()
print(set_a - set_b)

# frozenset
frozen = frozenset({10, 20, 30})
print(frozen)
# frozen.add(40)  # This would fail because frozenset is immutable

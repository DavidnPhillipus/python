 
# Python String Formatting 
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings. 
price = 59 
txt = f"The price is {price} dollars" 
print(txt) 


# A modifier is included by adding a colon : followed by a legal formatting type, like .2f which 
# means fixed point number with 2 decimals: 
txt = f"The price is {price:.2f} dollars" 
print(txt)


# Perform Operations in F-Strings
tax = 0.25 
txt = f"The price is {price + (price * tax)} dollars"


# You can perform if...else statements inside the placeholders: 
# Return "Expensive" if the price is over 50, otherwise return "Cheap": 
price = 49 
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}" 

# You can execute functions inside the placeholder: 
fruit = "apples" 
txt = f"I love {fruit.upper()}" 
print(txt)


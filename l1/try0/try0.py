import mymodule
print(mymodule.person1["age"])
# or 
from mymodule import person1
print (person1["age"])


# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# json.dumps(x, indent=4)
# # the parameter indent=space in linne, sort -ab
# print(json.dumps(x, indent=4, sort_keys=True))

import re


import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

# import platform
# x = dir(platform)
# print(x)

# username = input("Enter username:")
# print("Username is: " + username)

price = 59
txt = f"The price is {price} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

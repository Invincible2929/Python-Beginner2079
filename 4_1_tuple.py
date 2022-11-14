male = ["ram", "hari", "shyam"]
male.append("ravi")
print(male)
"""
Tuple is a data structure that stores more than one value at a time.
However, unlike list values, in tuple, items cannot be added or removed.
"""

female = ("sita", "gita", "rita")
print(female)
# to add or remove values in tuple, we need to convert tuple into list.
fem = list(female)
print(fem)
no = female.count("gita")
print(no)
length = len(female)
print(length)

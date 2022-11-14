person = {"name": "ram", "age": 20, "city": "kathmandu"}
# selecting the value of dictionary using index
person_name = person["name"]
person_age = person["age"]
person_city = person["city"]

print(person_name)
print(person_age)
print(person_city)

# updating the value of dictionary item
person["city"] = "Pokhara"
print(person)
person["age"] = 25
print(person)

# we can also use the update function
person.update({"name": "harry"})
print(person)

# removing the item from dictionary
person.pop("name")
print(person)

# adding item to the dictionary
person["country"] = "Nepal"
print(person)
person["email"] = "abcd12@gmail.com"
print(person)

info = {"name": "hero", "height": 6, "weight": 60, "food": "momo"}
info_name = info["name"]
info_height = info["height"]
info_weight = info["weight"]
info_food = info["food"]

print(info_name)
print(info_height)
print(info_weight)
print(info_food)

info.update({"name": "zero"})
print(info)

info.pop("name")
print(info)

info["email"] = "xyz@gmail.com"
print(info)

info["weight"] = 70
print(info)

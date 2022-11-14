'''
Variable: data structure that stores one value at a time, however its value can change during program execution.
'''
'''
Rules for naming variables:
-capitalization matters. ie. small x and capital X are different variables
-variable names always start with alphabets or underscore (_)
-variable names cannot contain special characters. eg: @, ?
-variable names can be of any length.
'''
x = 4

print(x)
x = x + 1
print(x)

y = 2
z = x % y
print(z)

first_name = "ram "
print(first_name)

last_name = "shrestha"
print(last_name)
# concatenation is the process of combining two or more string together.

space = " "

print(first_name + space + last_name)

print(first_name + (" ") + last_name)

print("my name is " + first_name + space + last_name)

print("my name is " + first_name + (" ") + last_name + " Hi")



# for single condition
x = 100
if x == 10:
    print("hi")

if x == 100:
    print("hello")

name = "ram"
if name == "ram":
    print("This is Ram Shrestha")

# 2 conditions
x = 5
if x == 1:
    print("x is equals to 1")
else:
    print("x is not 1")

# multiple conditions
if x == 1:
    print("x is equals to 1")
elif x == 2:
    print("x is equals to 2")
elif x == 3:
    print("x is equals to 3")
elif x == 4:
    print("x is equals to 4")
else:
    print("x is not equals to 1,2,3 or 4")

x = "D"
if x == "A":
    print("first division")
elif x == "B":
    print("second division")
elif x == "C":
    print("third division")
elif x == "D":
    print("fail")

marks = 40
if 80 <= marks <= 100:
    print("A")
elif 60 <= marks <= 59:
    print("B")
elif 40 < marks <= 59:
    print("C")
elif 0 <= marks <= 40:
    print("D")
else:
    print("you cannot score such number")

# Write a program to find maximum between two numbers
x = 3
y = 6
if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")

# maximum between 3 numbers
x = 30
y = 20
z = 5
if x > y > z:  # or y<x>z
    print("x is greater than y and z")
elif y > x > z:
    print("y is greater than x and z")
else:
    print("z is greater than x and y")

# check if number is positive or negative or zero
x = -8
if x == 0:
    print("the number is zero")
elif x > 0:
    print("the number is positive")
elif x < 0:
    print("the number is negative")

# check whether a number is divisible by 5 or not
y = 11
if y % 5 == 0:
    print("the number is divisible by 5")
else:
    print("the number is not divisible by 5")

# check whether an area is square or rectangle
length = 3
breadth = 2
if length == breadth:
    print("the area is square")
else:
    print("the area is rectangle")

# check whether tha number is odd or even
x = 99
if x % 2 == 0:
    print("the number is even")
elif x == 0:
    print('neither odd nor even')
else:
    print("the number is odd")

# checking the existence of letter 'a' in apple
fruit = "apple"
if 'a' in fruit:
    print("Yes, the letter a is present")
else:
    print("No, the letter a is not present")

# nested if else
x = 9
y = 5
if x < 10:
    if y < 10:
        print("hello")
    else:
        print("bye")
else:
    print("x is not less than 10")

# multiple if
country = "Nepal"
city = "Kathmandu"
if country == "Nepal":
    if city == "Kathmandu":
        print("The person is in Nepal, Kathmandu")
    else:
        print("The person is in Nepal but outside Kathmandu valley")
elif country == "India":
    if city == "Delhi":
        print("The person is in India and lives in capital Delhi")
    else:
        print("THe person is in India but outside the capital")
else:
    print("The person is neither in Nepal nor in India")


shape = "rectangle"
size = 700
if shape == "rectangle":
    if size <= 500:
        print("football field")
elif shape == "circle":
    if size <= 600:
        print("cricket field")
else:
    print("nothing")


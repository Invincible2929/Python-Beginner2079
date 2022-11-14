# looping
x = 10
while x >= 1:
    print(x)
    x = x - 1

x = 1
while x <= 10:
    print("hi")
    x = x + 1

x = -5
while x <= -1:
    print(x)
    x = x + 1

x = 1
while x <= 10:
    if x % 2 == 0:
        print("hi")
    else:
        print("hello")
    x = x + 1

# print 1 2 hi 4 5
x = 1
while x <= 5:
    if x == 3:
        print("hi")
    else:
        print(x)
    x = x + 1

# print 1 2 3 hi 4 5
x = 1
while x <= 5:
    if x == 4:
        print("hi")
    print(x)
    x = x + 1

# print all 1 3 4 7 8 9 10
x = 1
while x <= 10:
    if x == 2:
        pass
    elif x == 5:
        pass
    else:
        print(x)
    x = x + 1

# count odd and even number between 1 to 100
i = 1
even = 0
odd = 0
while i <= 100:
    if i % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    i = i + 1
print(even, odd)

# sum of first 10 numbers
x = 1
sum = 0
while x <= 10:
    sum = sum + x
    x = x + 1
print(sum)

# make list [1 2 3 4 5]
list = []
x = 1
while x <= 5:
    list.append(x)
    x = x + 1
print(list)

# make list [1 2 hi 4 5]
list = []
x = 1
while x <= 5:
    if x == 3:
        list.append("hi")

    else:
        list.append(x)
    x = x + 1
print(list)

# shape-rectangle size-500 = football or shape-circle size-600 = cricket else nothng

shape = "rectangle"
size = 600
if size >= 500 and shape == "rectangle":
    print("football field")
elif shape == "circle" and size >= 600:
    print("cricket field")
else:
    print("nothing")

x = 1
while x <= 5:
    if x == 3:
        print("hi")
        print(x)
    elif x == 5:
        print("hello")
        print(x)
    else:
        print(x)
    x = x + 1

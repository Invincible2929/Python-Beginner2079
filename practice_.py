"""""
no = [2, 5, 4, 2]
no.pop(0)
print(no)
no.pop(0)
print(no)

name = ["aadey", "mula", "hero"]
print(name[0])

name.append("goru")
print(name)

name.pop(2)
print(name)
name.remove("goru")
print(name)

print(name[1])
sum = (name[0] + name[1])
print(sum)

add = (no[0] + no[(1)])
print(add)

name.insert(0, "hello")
print(name)

name[0] = "hi"
print(name)

list = ["hey", "say", "they"]
gist = ["so", "what", "you"]
combine = list + gist
print(combine)

x = 1
while x <= 3:
    print(x)
    x = x + 1

x = 1
while x <= 3:
    if x == 3:
        print("Hi")
    else:
        print(x)
    x = x + 1
"""""
"""""
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
x = 1
while x <= 100:
    if x % 2 == 0:
        print(x)
    x = x + 1
"""
"""""
# x=10 y>0 positive x=10 y<0 negative
x = 10
y = -1
if x == 10 and y > 0:
    print("both x and y are positive")
elif x == 10 and y < 0:
    print("x is positive but y is negative")

x = 10
y = -1
if x == 10:
    if y > 0:
        print("x and y are positive")
    else:
        print("x is positive but y is negative")

fruit = "apple"
if "o" in fruit:
    print("a is present in fruit")
else:
    print("a is not in fruit")

list = [1, 2, 3, 4]
if 2 in list:
    print("2 is in the list")

name = ["ram", "shyam", "hari", "sita"]
if "ram" in name:
    print("ram in the list")
else:
    print("not in the list")

name = ["ram", "hari", "sita"]
word = input("enter your name: ")
if word in name:
    print(word + " is in the list")
else:
    print(word + " is not in the list")
"""
"""""
x = 1
while x <= 100:
    print(x)
    x = x + 2

x = -5
while x <= -1:
    print(x)
    x = x + 1

x = 1
while x <= 100:
    if x % 2 == 0:
        print(x)
    x = x + 1

x = 1
while x <= 5:
    if x == 3:
        print("hi")
    else:
        print(x)
    x = x + 1

x = 1
while x <= 5:
    if x == 3:
        print("hi")
    print(x)
    x = x + 1

x = -1
while x >= -5:
    print(x)
    x = x - 1

x = 1
while x <= 10:
    if x % 2 == 0:
        print("hi")
    else:
        print("hello")
    x = x + 1

x = 1
sum = 0
while x <= 10:
    sum = sum + x
    x = x + 1
print(sum)

x = 1
even = 0
odd = 0
while x <= 10:
    if x % 2 == 0:
        odd = odd + 1
    else:
        even = even + 1
    x = x + 1
print(odd, even)

x = 0
while x <= 10:
    print(x)
    x = x + 2
"""

# count the specific letter 'e' in the word
x = "teste"
no = x.count("e")
print(no)

# print the cube of numbers from 1 to specific number
x = 1
while x <= 5:
    y = x ** 3
    print(y)
    x = x + 1

# list=[3,5,7,2,5] reverse this list
# list=[4,7,3,5,7,9] print numbers of even index
# print the multiplication table

list = [3, 5, 7, 2, 5]
newlist = []
length = len(list) - 1
x = 0
while x <= length:
    newlist.insert(0, list[x])
    x = x + 1
print(newlist)

list = [4, 7, 3, 5, 7, 9]
evenlist = []
length = len(list) - 1
x = 0
while x <= length:
    if x % 2 == 0:
        evenlist.append(list[x])
    x = x + 1
print(evenlist)

i = int(input("enter your number:"))
x = 1
while x <= 10:
    multiple = i * x
    print(i, "*", x, "=", multiple)
    x = x + 1

list = [1, 2, 3, 4, 5]
newlist = []
x = 0
while x <= 4:
    newlist.insert(0, list[x])
    x = x + 1
print(newlist)

x = 2
while x <= 11:
    if x == 4:
        pass
    else:
        print(x)
    x = x + 1

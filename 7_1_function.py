# Function will not get executed by itself.

def display_output():  # function define gareko
    print("hi")


display_output()  # function call gareko
display_output()


# function ma value add gareko
def addition(x, y):
    z = x + y
    print(z)


addition(6, 7)


def addition(x, y, i):
    z = x + y + i
    return z


j = addition(6, 7, 6)
print(j)


# example of function
def money_convert(amount, rate):
    value = amount * rate
    return value


new_value = money_convert(100, 120)
print(new_value)


# * infront of parameter allows us to put multiple value.
def add_numbers(*x):
    total = x[0] + x[1] + x[2] + x[3]
    print(total)


add_numbers(4, 6, 2, 3)


def add_numbers(*x):
    total = x[0] + x[1] + x[2] + x[3]
    return total


u = add_numbers(4, 6, 2, 3)
print(u)


def max_number(x, y, z):
    if y < x > z:
        print("x is the greatest")
    elif x < y > z:
        print("y is the greatest")
    else:
        print("z is the greatest")


max_number(7, 3, 4)


def add_list(*x):
    print(x[0] + x[1] + x[2] + x[3])


add_list(1, 2, 3, 4)


def max_number(x, y, z):
    if y < x > z:
        return x
    elif x < y > z:
        return y
    else:
        return z


total = max_number(1, 2, 3)
print(total)


def total(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum


print(total([4, 5]))


def product(numbers):
    multiply = 1
    for i in numbers:
        multiply = multiply * i
    return multiply


print(product([4, 5, 2]))

name
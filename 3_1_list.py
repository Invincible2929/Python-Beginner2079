"""
List is the data structure that holds more than one value at a time
The value in the list is changeable
List can contain duplicate value
"""
no = [10, 20, 5, 7, 8]

name = ["ram", "jay", "dibash", "safal", "rajib"]

birds = ["sparrow", "crow", "raven", "ostrich", "penguin"]

negative_no = [-2, -4, -6, -8, -10]

print(no)

print(no[0])
print(no[1])
print(no[2])
print(no[3])
print(no[4])

print(name[0])

sum = (no[2] + no[3])
print(sum)

total_sum = (no[0] + no[1] + no[1] + no[2] + no[3] + no[4])
print(total_sum)

no.append(40)  # append le list ko last ma number thapxa
no.append(60)
print(no)

no.insert(1, 9)  # insert le value lai list ko jata pani xirauna milxa
print(no)
no.insert(8, 80)
print(no)

no[0] = 1  # replacing the value at index 0, here, index no. use garera replace gareko xa
print(no)

no.remove(5)  # remove will eliminate the value that is encountered first
print(no)

no.pop(3)  # pop will eliminate the value at a given index. 7 hateko xa
print(no)
no.pop()  # pop ma kei index mention nagare list ko last value hatxa
print(no)

name.append("hari")
print(name)

name.insert(1, "rita")
print(name)
name[1] = "krita"
print(name)
name.remove("jay")
print(name)
name.pop(1)
print(name)

print(name[2])
print(name[0])
print("there are five persons" + " " + name[0] + ", " + name[1] + ", " + name[2] + ", " + name[3] + ", " + name[4])
print("there are three persons" + " " + name[0] + ", " + name[1] + ", " + name[2] + ".")

person = ["ram", "hari", "shyam"]
print(person[0] + " " + "and " + person[1] + " " + "are brothers and " + " " + person[2] + " " + "is their friend.")

x = len(person)  # len gives the length of the list
print(x)

y = person.count("ram")  # count() gives the number of repetation of an item in a list
print(y)

number = [1, 2, 3, 1, 6, 9, 1, 0, 1, 5, 1]
z = number.count(1)
print(z)

male = ["ram", "hari", "shyam"]
female = ["sita", "gita"]
male.extend(female)  # extend adds a new list to the existing list
print(male)

combine = male + female  # + combines two lists to give a new list
print(combine)

indexno = male.index("hari")  # index gives index no. of an item in a list.
print(indexno)

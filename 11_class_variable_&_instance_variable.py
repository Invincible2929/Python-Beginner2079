# # class Family:
# #     father = "ram" #class variable
# #     def __init__(self, sname):
# #         self.name = sname # obj variable
# #
# # a = Family("rama")
# # b = Family("hari")
# # c = Family("mohan")
# # a.name = "jack"
# # print(a.name)
# # print(b.name)
# # print(c.name)
# #
# # # a.father = "harry" #changes class varible into instance variable in python
# # print(a.father)
# # print(b.father)
# # print(c.father)
# #
# # Family.father = "sunny" #class variable ko value change garda sab obj ko change hunxa
# # print(a.father)
# # print(b.father)
# # print(c.father)
#
# class Family:
#     father = "hari"
#
#     def __init__(self, sname):
#         self.name = sname
#
#
# a = Family("rama")
# b = Family("jojo")
# c = Family("harry")
#
# print(a.name)
# print(b.name)
# print(c.name)
#
# print(a.father)
# print(b.father)
#
# a.father = "john"  # obj variable ko value change garda jun obj ko change gareko tyo matra change hunxa.
# print(c.father)
#
# Family.father = "hero"  # class variable ko value change garda sab obj ko change hunxa.
# print(a.father)
# print(b.father)
# print(c.father)
#
#
# def add():
#     print("hi")

#
# sum = add
# sum()

def a(x):
    return x + 4
def b(x):
    return x - 4
def mixed(y, x):
    result = y(x)
    return result

print(mixed(b,5))
print(mixed(a,5))

# class is a blueprint or a concept.
# class contains any no. of properties and funtion.
class Human:
    def __init__(self):  # constructor function gets executed during object creation.
        print("This is consructor function")

    def walk(self):
        print("Human can walk")

    def speak(self):
        print("Human can speak")
    def eat(self,sjack):
        self.__jack = sjack


ram = Human()
srijan = Human()
hari = Human()
ram.walk()
srijan.walk()
hari.walk()


# class bird:
#     def fly(self):
#         print("bird can fly")
#
#     def eat(self):
#         print("bird can eat")
#
#
# sparrow = bird()
# sparrow.fly()
# sparrow.eat()
# raven = bird()
# raven.fly()
# raven.eat()
#
#
# class Human:
#     def walk(self, x):
#         x = x + 1
#         return x
#
#
# shyam = Human()
# y = shyam.walk(6)
# print(y)
#
#
# class a:
#     x = 3
#
#     def a1(self):
#         global x
#         x = 2
#         print(x)
#
#     def a2(self):
#         print(x)
#         print(self.x)  # self.x is for global
#
#
# obja = a()
# obja.a1()
# obja.a2()

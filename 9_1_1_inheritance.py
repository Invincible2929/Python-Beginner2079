class Human:  # parent class
    def __init__(self):
        print("constructor of human")
    def walk(self):
        print("hi")

    def speak(self):
        print("hello")


ram = Human()
ram.walk()


class Male(Human):  # child class
    def __init__(self):
        super().__init__()
        print("man confuse")
    def dominate(self):
        print("male superior")

    def pp(self):
        print("strong male")

    def walk(self):  # sub class function will override the parent class function.
        super().walk()
        print("function override")
    def speak(self):
        print("function override")

objmale = Male()
objmale.walk()  # child class object can call parent class function as well.
objmale.speak()
objme = Male()
objme.dominate()
objme.pp()
objmale.dominate()
objmale.walk()  # sub class function will override the parent class function.
objme.speak()






# class animal:
#     def hunt(self):
#         print("animal can hunt")
#     def eat(self):
#         print("animal can eat")
#     def walk(self):
#         print("hello")
#
# lion = animal()
# lion.hunt()
# cow = animal()
# cow.eat()
# cow.walk()
#
# class wild(animal):
#     def aggressive(self):
#         print("wild animals are aggressive")
#     def walk(self):
#         super().walk()
#         print("no override")
# tiger = wild()
# tiger.aggressive()
# tiger.eat()
# tiger.walk()
#
#

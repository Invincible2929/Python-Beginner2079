# # # # # # class robots:
# # # # # #     def __init__(self):
# # # # # #         print("constructor function")
# # # # # #     def intelligent(self):
# # # # # #         print("robots are intelligent")
# # # # # #     def hard(self):
# # # # # #         print("robots are hard")
# # # # # #     def man_made(self):
# # # # # #         print("robots are man made")
# # # # # #
# # # # # # mark1 = robots()
# # # # # # mark1.intelligent()
# # # # # # mark1.hard()
# # # # # # mark1.man_made()
# # # # # #
# # # # # # class mini_robots(robots):
# # # # # #     def __init__(self):
# # # # # #         super().__init__()
# # # # # #         print("constructor funtion ho mula")
# # # # # #     def operate(self):
# # # # # #         print("mini robots can operate")
# # # # # #     def small(self):
# # # # # #         print("mini robots are small")
# # # # # #     def man_made(self):
# # # # # #         print("mini robots pani man made ho")
# # # # # #     def hard(self):
# # # # # #         super().hard()
# # # # # #         print("mini robots pani hard hunxa")
# # # # # #
# # # # # # mark2 = mini_robots()
# # # # # # mark2.man_made()
# # # # # # mark2.hard()
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # # #
# # # # #
# # # # # class Car:
# # # # #
# # # # #     def __init__(self):
# # # # #         self.__updateSoftware()
# # # # #
# # # # #     def drive(self):
# # # # #         print('driving')
# # # # #
# # # # #     def __updateSoftware(self):
# # # # #         print('updating software')
# # # # #
# # # # # redcar = Car()
# # # # # redcar.drive()
# # # #
# # # class Car:
# # #
# # #     def __init__(self):
# # #         self.maxspeed = 200  # without __ yo private hudaina ani value change garna milxa. see line 65.
# # #         self.__name = "Supercar"  # __ paxi yo private hunxa ra yeslai change or arule access garna paudaina. see line 66
# # #
# # #     def drive(self):
# # #         print('driving. maxspeed ' + str(self.maxspeed) + " " + str(self.__name))
# # #
# # #
# # # redcar = Car()
# # # redcar.drive()
# # # redcar.maxspeed = 100  # will change variable because it's not private
# # # redcar.__name = "Ecar" # will not change variable because it's private
# # # redcar.drive()
# #
# # class Point:
# #     def __init__(self):
# #         print("hi")
# #     def fn1(self):
# #         print("hello")
# #     def fn2(self):
# #         print("sup")
# #
# # obj = Point()
# # obj.fn2()
#
#
#
# class Family:
#     father = "ram" #class variable
#     def fn(self, sname):
#         self.name = sname # obj variable
#         return sname
#
# a = Family()
# b = a.fn("ram")
# print(a)
#
#
#
# # print(a.name)
# # print(b.name)
# # print(c.name)
# #
# # # a.father = "harry" #changes class varible into instance variable in python
# # print(a.father)
# # print(b.father)
# # print(c.father)
#
# def ad():
#     return 3
# print(ad())



class Details:
    def setInfo(self, sname, semail, scity, ssalary):
        self.__name = sname
        self.__email = semail
        self.__city = scity
        self.__salary = ssalary


    def getInfo(self):
        return f"Name: {self.__name}, \nEmail: {self.__email}, \ncity: {self.__city}, \nsalary: {self.__salary}"


objHuman = Details("ram", "ram123@gmail.com", "ktm", 2500)
print(objHuman.__name())


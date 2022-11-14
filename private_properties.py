# class Human:
#     i = 10
#
#     def __init__(self, x):
#         self.__i = x  # making the attribute private.
#         print("Constructor")
#
#     def walk(self):
#         print("walk")
#
#
# objHuman = Human(60)
# print(objHuman.i)
#

class Human:
    def __init__(self, x):
        self.publicvar = 20
        self.__privatevar = x
        print("constructor")

    def setterPrivatevar(self, x):
        self.__privatevar = x

    def getterPrivatevar(self):
        return self.__privatevar


objHuman = Human(60)
objHuman.setterPrivatevar(22)
print(objHuman.getterPrivatevar())

class Office:
    def setFirstName(self,fname):
        self.name = fname
    def setLastName(self,lname):
        self.name

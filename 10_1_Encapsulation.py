# class Human:
#     def setName(self, sname):
#         self.__name = sname
#
#     def getName(self):
#         return self.__name
#
#
# objHuman = Human()
# objHuman.setName("ram")
# name = objHuman.getName()
# print(name)

#
# class Details:
#     def setInfo(self, sname, semail, scity, ssalary):
#         self.__name = sname
#         self.__email = semail
#         self.__city = scity
#         self.__salary = ssalary
#
#
#     def getInfo(self):
#         return f"Name: {self.__name}, \nEmail: {self.__email}, \ncity: {self.__city}, \nsalary: {self.__salary}"
#
#
# objHuman = Details()
# objHuman.setInfo("ram", "ram123@gmail.com", "ktm", 2500)
# info = objHuman.getInfo()
# print(info)
#
# class Human:
#     def setFirstName(self, fname):
#         self.__firstName = fname
#     def getFirstName(self):
#         return self.__firstName
#     def setLastName(self, lname):
#         self.__lastName = lname
#     def getLastName(self):
#         return self.__lastName
#     def setCity(self, scity):
#         self.__city = scity
#     def getCity(self):
#         return self.__city
#     def setEmail(self, semail):
#         self.__email = semail
#     def getEmail(self):
#         return self.__email
#     def setAge(self, sage):
#         self.__age = sage
#     def getAge(self):
#         return self.__age
#
#
# objHuman = Human()
# objHuman.setFirstName("ram")
# objHuman.setLastName("Sharma")
# objHuman.setCity("KTM")
#
# print(objHuman.getFirstName())
# print(objHuman.getLastName())
# print(objHuman.getCity())


class Office:
    def setName(self,sname):
        self.__name = sname
    def getName(self):
        return self.__name
    def setRole(self,srole):
        self.__role = srole
    def getRole(self):
        return self.__role
    def setSalary(self, ssalary):
        self.__salary = ssalary
    def getSalary(self):
        return self.__salary


obj = Office()
obj.setName("Sushil")
obj.setRole("Administrator")
obj.setSalary(50000)

print(obj.getName())
print(obj.getRole())
print(obj.getSalary())


















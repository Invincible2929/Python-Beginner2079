class Human:
    def __init__(self, sname, scity):
        self.name = sname
        self.city = scity

    def walk(self):
        print("Human walk")
        print(self.__city)



objHuman = Human("ram", "ktm")
print(objHuman.name)
print(objHuman.city)
# private property(variable) lai class bahira object le call garna paudaina, class vitra pauxa.



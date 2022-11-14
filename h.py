class human:
    def __init__(self):
        print("hello")


ram = human()

class male(human):
    def __init__(self):
        super().__init__()
        print("hi")

hari = male()



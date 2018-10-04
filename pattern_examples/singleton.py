# Singleton is a class that only instantiates one object in the application

class Singleton(object):
    _instance = None
    def __new__(cls, *kwargs):
        if Singleton._instance is None:
            Singleton._instance = object.__new__(cls)

        return Singleton._instance

    def __init__(self, value, value2):
        self.value = value
        self.value2 = value2

a = Singleton(10, 11)
print("First instance: \n\t", a)
print("\tValue 1: ", a.value, "\n\tValue 2: ", a.value2)

b = Singleton(11, 12)
print("Second instance: \n\t", b, b.value2)
print("\tValue 1: ", b.value, "\n\tValue 2: ", b.value2)

c = Singleton(12, 13)
print("Third instance: \n\t", c, c.value2)
print("\tValue 1: ", c.value, "\n\tValue 2: ", c.value2)
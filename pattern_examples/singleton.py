# Singleton is a class that only instantiates one object in the application
from django.core.files import File

class Singleton(object):
    _instance = None
    _file = None
    def __new__(cls, *kwargs):
        if Singleton._instance is None:
            Singleton._instance = object.__new__(cls)

        if Singleton._file is None:
            print("There was no opened file. Opening a new one")
            f = open('example.txt', 'w')
            Singleton._file = File(f)

        return Singleton._instance

    def __init__(self, value, value2):
        self.value = value
        self.value2 = value2
        Singleton._file.write('My values are {0} and {0}\n'.format(self.value, self.value2))

a = Singleton(10, 11)
print("First instance: \n\t", a)
print("\tValue 1: ", a.value, "\n\tValue 2: ", a.value2)

b = Singleton(11, 12)
print("Second instance: \n\t", b)
print("\tValue 1: ", b.value, "\n\tValue 2: ", b.value2)

c = Singleton(12, 13)
print("Third instance: \n\t", c)
print("\tValue 1: ", c.value, "\n\tValue 2: ", c.value2)

print("Check the 'example.txt' file to see how I can write to the same file even with many calls")
__author__ = 'rls'

class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hello, how are you? My name is ", self.name)

p = Person('Robin')
print(p)
p.say_hi()
# Object Orientated Programming in Python

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def add_one(self, x):
        return x + 1

    def bark(self):
        print("bark")


d = Dog("Tim", 34)
print(d.get_name())
d.set_age(23)
print(d.get_age())

d2 = Dog("Bill", 12)
print(d2.get_name())
print(d2.get_age())

dogs_name = ["Tim", "Bill"]
dogs_age = [32, 14]
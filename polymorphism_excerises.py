class Parent:
    def prn(self):
        print("Parent")


class Child(Parent):
    def __init__(self):
        self.a = Parent()

    def prn(self):
        print("Child")


temp = Child()
temp.a.prn()


# Parent Class
class Shape:
    sname = "Shape"

    def getName(self):
        return self.sname


# child class
class XShape(Shape):
    # initializer
    def __init__(self, name):
        self.xsname = name

    def getName(self):  # overriden method
        return (super().getName() + ", " + self.xsname)


circle = XShape("Circle")
print(circle.getName())


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def Animal_details(self):
        print("Name:", self.name)
        print("Sound:", self.sound)


class Dog(Animal):
    def __init__(self, name, sound, family):
        super().__init__(name, sound)
        self.family = family

    def Animal_details(self):
        super().Animal_details()
        print("Family:", self.family)


class Sheep(Animal):
    def __init__(self, name, sound, color):
        super().__init__(name, sound)
        self.color = color

    def Animal_details(self):
        super().Animal_details()
        print("Color:", self.color)


d = Dog("Pongo", "Woof Woof", "Husky")
d.Animal_details()
print("")
s = Sheep("Billy", "Baa Baa", "White")
s.Animal_details()


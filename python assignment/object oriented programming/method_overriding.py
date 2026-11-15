# Program to demonstrate method overriding

class Animal:
    def sound(self):
        print("Animals make different sounds")


class Dog(Animal):
    def sound(self):
        print("Dog says: Woof Woof")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow")


# Create objects
a = Animal()
d = Dog()
c = Cat()

# Call sound method
a.sound()
d.sound()
c.sound()

# Program to demonstrate multiple inheritance

class Teacher:
    def teaching(self):
        print("I am a Teacher")
        print("I teach students")


class Researcher:
    def research(self):
        print("I am a Researcher")
        print("I do research work")


class Professor(Teacher, Researcher):
    def display(self):
        print("I am a Professor")


# Create object of Professor
p = Professor()

p.display()
p.teaching()
p.research()

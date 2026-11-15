# Program to demonstrate hierarchical inheritance

class Shape:
    def display(self):
        print("This is a shape")


class Circle(Shape):
    def show_circle(self):
        print("This is a Circle")


class Rectangle(Shape):
    def show_rectangle(self):
        print("This is a Rectangle")


class Triangle(Shape):
    def show_triangle(self):
        print("This is a Triangle")


# Create objects
c = Circle()
r = Rectangle()
t = Triangle()

# Call methods
c.display()
c.show_circle()

r.display()
r.show_rectangle()

t.display()
t.show_triangle()
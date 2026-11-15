
# Program to use geometry package

from geometry import circle, rectangle

radius = float(input("Enter radius of circle: "))

print("Area of Circle:", circle.area(radius))

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

print("Area of Rectangle:", rectangle.area(length, width))

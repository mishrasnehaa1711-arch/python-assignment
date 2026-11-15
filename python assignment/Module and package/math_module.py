
# Program to perform mathematical operations using math module

import math

num = int(input("Enter a number: "))

print("Square Root:", math.sqrt(num))

power = int(input("Enter power: "))
print("Power:", math.pow(num, power))

print("Factorial:", math.factorial(num))

angle = float(input("Enter angle in degrees: "))

radian = math.radians(angle)

print("Sin value:", math.sin(radian))
print("Cos value:", math.cos(radian))
print("Tan value:", math.tan(radian))

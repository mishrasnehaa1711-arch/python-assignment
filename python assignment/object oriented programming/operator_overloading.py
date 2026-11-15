# Program to demonstrate operator overloading

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        real_part = self.real + other.real
        imaginary_part = self.imaginary + other.imaginary

        return Complex(real_part, imaginary_part)

    def display(self):
        print(self.real, "+", self.imaginary, "i")


# Create two complex numbers
num1 = Complex(5, 3)
num2 = Complex(2, 4)

# Add two complex numbers using +
result = num1 + num2

print("First complex number:")
num1.display()

print("Second complex number:")
num2.display()

print("Sum of complex numbers:")
result.display()
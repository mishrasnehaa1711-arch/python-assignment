
# Program to find power of a number using recursion

def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


num = int(input("Enter the base number: "))
exp = int(input("Enter the power: "))

if exp < 0:
    print("Please enter a non-negative power")
else:
    result = power(num, exp)
    print("Result:", result)

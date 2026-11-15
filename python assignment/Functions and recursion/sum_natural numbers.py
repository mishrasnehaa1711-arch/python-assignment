
# Program to find sum of natural numbers using recursion

def natural_sum(n):
    if n == 0:
        return 0
    else:
        return n + natural_sum(n - 1)


num = int(input("Enter a number: "))

if num < 0:
    print("Please enter a positive number")
else:
    result = natural_sum(num)
    print("Sum of first", num, "natural numbers is:", result)

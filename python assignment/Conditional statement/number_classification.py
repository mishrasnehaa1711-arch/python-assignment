
num = int(input("Enter a number: "))

# Positive, Negative or Zero
if num > 0:
    print("Positive Number")

elif num < 0:
    print("Negative Number")

else:
    print("Zero")

# Even or Odd
if num % 2 == 0:
    print("Even Number")

else:
    print("Odd Number")

# Divisibility by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")

else:
    print("Not divisible by both 3 and 5")

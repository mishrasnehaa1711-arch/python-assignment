
# Program to perform operations using random module

import random
import string

# Generate OTP
otp = random.randint(100000, 999999)
print("Your OTP is:", otp)

# Generate Random Password
characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for i in range(8))
print("Random Password:", password)

# Generate Random List Numbers
numbers = []

for i in range(5):
    num = random.randint(1, 100)
    numbers.append(num)

print("Random List:", numbers)

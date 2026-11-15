
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find HCF
hcf = 1

for i in range(1, min(num1, num2) + 1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

# Find LCM
lcm = 1

while True:
    if lcm % num1 == 0 and lcm % num2 == 0:
        break
    lcm = lcm + 1

print("HCF =", hcf)
print("LCM =", lcm)

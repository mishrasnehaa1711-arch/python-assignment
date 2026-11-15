
num = int(input("Enter a number: "))

square = num ** 2

temp = num
count = 1

while temp > 0:
    count = count * 10
    temp = temp // 10

if square % count == num:
    print(num, "is an Automorphic Number")
else:
    print(num, "is not an Automorphic Number")

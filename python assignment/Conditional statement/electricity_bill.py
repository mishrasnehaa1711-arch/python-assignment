
units = int(input("Enter electricity units consumed: "))

if units <= 100:
    bill = units * 5

elif units <= 300:
    bill = (100 * 5) + (units - 100) * 7

else:
    bill = (100 * 5) + (200 * 7) + (units - 300) * 10

if bill > 2000:
    bill = bill + (bill * 5 / 100)

print("Total Electricity Bill =", bill)

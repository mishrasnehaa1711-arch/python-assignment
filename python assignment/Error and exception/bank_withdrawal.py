
# Program for Bank Withdrawal System

balance = 5000

print("Welcome to Bank")

print("Available Balance:", balance)

amount = int(input("Enter withdrawal amount: "))

try:
    if amount > balance:
        raise Exception("Insufficient balance!")

    balance = balance - amount

    print("Withdrawal successful!")
    print("Remaining Balance:", balance)

except Exception as e:
    print("Error:", e)

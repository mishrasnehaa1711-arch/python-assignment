
# Program for Age Validation System

age = int(input("Enter your age: "))

try:
    if age < 18:
        raise Exception("Age must be 18 or above")

    print("You are eligible!")

except Exception as e:
    print("Error:", e)

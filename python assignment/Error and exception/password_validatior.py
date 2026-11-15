
# Program for Password Validation

try:
    password = input("Enter your password: ")

    if len(password) < 8:
        raise Exception("Password must contain at least 8 characters")

    if not any(char.isupper() for char in password):
        raise Exception("Password must contain an uppercase letter")

    if not any(char.isdigit() for char in password):
        raise Exception("Password must contain a number")

    print("Password is valid!")

except Exception as e:
    print("Error:", e)

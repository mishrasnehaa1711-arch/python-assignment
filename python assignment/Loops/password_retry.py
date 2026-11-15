
correct_password = "python123"
attempts = 0

while attempts < 3:
    password = input("Enter your password: ")

    if password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts = attempts + 1
        print("Wrong Password!")

if attempts == 3:
    print("Account Blocked!")

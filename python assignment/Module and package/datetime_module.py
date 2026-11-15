
# Program to use datetime module

import datetime

# Display current date and time
today = datetime.datetime.now()

print("Current Date:", today.date())
print("Current Time:", today.time().strftime("%H:%M:%S"))

# Calculate age
birth_year = int(input("Enter your birth year: "))

current_year = today.year

age = current_year - birth_year

print("Your Age is:", age)

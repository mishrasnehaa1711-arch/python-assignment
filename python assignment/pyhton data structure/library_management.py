
# Program for Library Management using Dictionary

library = {
    "Python": 5,
    "Java": 3,
    "C Programming": 4,
    "Data Science": 2
}

print("Welcome to Library Management System")

print("\nAvailable Books:")

for book, quantity in library.items():
    print(book, ":", quantity)

# Add a new book
new_book = input("\nEnter book name to add: ")
quantity = int(input("Enter book quantity: "))

if new_book in library:
    library[new_book] += quantity
else:
    library[new_book] = quantity

print("\nUpdated Library:")

for book, quantity in library.items():
    print(book, ":", quantity)

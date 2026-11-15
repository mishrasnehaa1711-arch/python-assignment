
# Program to rotate a list left or right

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

k = int(input("Enter positions to rotate: "))

choice = input("Enter L for Left or R for Right: ")

k = k % len(numbers)

if choice == 'L' or choice == 'l':
    numbers = numbers[k:] + numbers[:k]

elif choice == 'R' or choice == 'r':
    numbers = numbers[-k:] + numbers[:-k] if k != 0 else numbers

else:
    print("Invalid choice!")

print("Final List:", numbers)

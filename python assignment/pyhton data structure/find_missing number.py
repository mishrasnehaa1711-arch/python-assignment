
# Program to find the missing number in a list

numbers = [1, 2, 3, 5, 6, 7]

n = 7

total = n * (n + 1) // 2

list_sum = sum(numbers)

missing_number = total - list_sum

print("Original List:", numbers)
print("Missing Number is:", missing_number)

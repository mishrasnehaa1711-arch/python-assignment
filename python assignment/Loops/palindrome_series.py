
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Palindrome numbers are:")

for num in range(start, end + 1):
    temp = num
    reverse = 0

    while temp > 0:
        digit = temp % 10
        reverse = reverse * 10 + digit
        temp = temp // 10

    if num == reverse:
        print(num)


text = input("Enter a string: ")

text = text.replace(" ", "").lower()

reverse = text[::-1]

if text == reverse:
    print("Palindrome String")
else:
    print("Not a Palindrome String")

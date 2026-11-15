
# Program to reverse a string using recursion

def reverse_string(text):
    if len(text) == 0:
        return text
    else:
        return reverse_string(text[1:]) + text[0]


word = input("Enter a string: ")

result = reverse_string(word)

print("Original String:", word)
print("Reversed String:", result)

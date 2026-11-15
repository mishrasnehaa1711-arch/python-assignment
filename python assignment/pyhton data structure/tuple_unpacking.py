
# Program to swap first and last elements of a tuple

my_tuple = (10, 20, 30, 40, 50)

print("Original Tuple:", my_tuple)

first, *middle, last = my_tuple

my_tuple = (last, *middle, first)

print("Tuple after swapping:", my_tuple)

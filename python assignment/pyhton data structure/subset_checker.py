
# Program to check whether one set is a subset of another

set1 = {10, 20, 30, 40, 50}

set2 = {20, 30, 40}

print("First Set:", set1)
print("Second Set:", set2)

if set2.issubset(set1):
    print("Set2 is a subset of Set1")
else:
    print("Set2 is not a subset of Set1")

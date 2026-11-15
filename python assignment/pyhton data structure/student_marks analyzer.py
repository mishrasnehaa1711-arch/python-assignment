
# Program to analyze student marks

students = {
    "Rahul": 85,
    "Priya": 92,
    "Aman": 35,
    "Neha": 76,
    "Riya": 28
}

print("Student Marks:")
for name, marks in students.items():
    print(name, ":", marks)

# Find topper
topper = max(students, key=students.get)

# Calculate average marks
average = sum(students.values()) / len(students)

# Count failures
failures = 0

for marks in students.values():
    if marks < 33:
        failures += 1

print("\nTopper:", topper)
print("Highest Marks:", students[topper])
print("Average Marks:", average)
print("Number of Failures:", failures)

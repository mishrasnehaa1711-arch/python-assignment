# Program to demonstrate private variable

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_details(self):
        print("Employee Name:", self.name)
        print("Employee Salary:", self.__salary)


# Create employee object
emp = Employee("Sneha", 30000)

# Display employee details
emp.show_details()
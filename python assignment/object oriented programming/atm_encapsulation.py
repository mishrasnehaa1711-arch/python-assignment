# Program to demonstrate ATM system using encapsulation

class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_balance(self, entered_pin):
        if entered_pin == self.__pin:
            print("Your balance is:", self.__balance)
        else:
            print("Wrong PIN!")

    def withdraw(self, entered_pin, amount):
        if entered_pin == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                print("Please collect your cash.")
                print("Remaining balance:", self.__balance)
            else:
                print("Insufficient balance!")
        else:
            print("Wrong PIN!")


# Create ATM object
my_atm = ATM(1234, 10000)

# Perform ATM operations
my_atm.check_balance(1234)
my_atm.withdraw(1234, 2000)
my_atm.check_balance(1234)
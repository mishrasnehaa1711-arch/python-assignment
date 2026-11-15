
# Program to demonstrate multilevel inheritance

class Vehicle:
    def vehicle_info(self):
        print("This is a Vehicle")


class Car(Vehicle):
    def car_info(self):
        print("This is a Car")


class ElectricCar(Car):
    def electric_info(self):
        print("This is an Electric Car")


# Create object of ElectricCar
my_car = ElectricCar()

my_car.vehicle_info()
my_car.car_info()
my_car.electric_info()

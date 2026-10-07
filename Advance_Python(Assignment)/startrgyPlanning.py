class Bike:
    def travel(self):
        print("Travelling by Bike")


class Car:
    def travel(self):
        print("Travelling by Car")


class Bus:
    def travel(self):
        print("Travelling by Bus")


class Travel:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def start_journey(self):
        self.vehicle.travel()


print("Select Vehicle")
print("1. Bike")
print("2. Car")
print("3. Bus")

choice = int(input("Enter Choice: "))

if choice == 1:
    journey = Travel(Bike())
elif choice == 2:
    journey = Travel(Car())
elif choice == 3:
    journey = Travel(Bus())
else:
    print("Invalid Choice")
    exit()

journey.start_journey()
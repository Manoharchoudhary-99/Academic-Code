class Vehicle:

    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

    def get_category(self):
        if self.price >= 1000000:
            return "Luxury"
        else:
            return "Economy"

    def show_details(self):
        print(f"Vehicle Number : {self.vehicle_number}")
        print(f"Brand          : {self.brand}")
        print(f"Price          : ₹{self.price}")
        print(f"Category       : {self.get_category()}")
        print("-" * 35)


class Showroom:

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"{vehicle.brand} added successfully.")

    def display_vehicles(self):
        if len(self.vehicles) == 0:
            print("No vehicles available.")
        else:
            print("\n------ Vehicle Details ------")
            for vehicle in self.vehicles:
                vehicle.show_details()


# Main Program

showroom = Showroom()

showroom.add_vehicle(Vehicle("MH12AB1234", "BMW", 6200000))
showroom.add_vehicle(Vehicle("MH14CD5678", "Maruti Suzuki", 850000))
showroom.add_vehicle(Vehicle("MH01EF9012", "Hyundai", 1200000))

showroom.display_vehicles()

# output:
# BMW added successfully.
# Maruti Suzuki added successfully.
# Hyundai added successfully.

# ------ Vehicle Details ------
# Vehicle Number : MH12AB1234
# Brand          : BMW
# Price          : ₹6200000
# Category       : Luxury
# -----------------------------------
# Vehicle Number : MH14CD5678
# Brand          : Maruti Suzuki
# Price          : ₹850000
# Category       : Economy
# -----------------------------------
# Vehicle Number : MH01EF9012
# Brand          : Hyundai
# Price          : ₹1200000
# Category       : Luxury
# -----------------------------------
class Mobile:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

    def display(self):
        print(f"Brand    : {self.brand}")
        print(f"Model    : {self.model}")
        print(f"Price    : ₹{self.price}")
        print(f"Category : {self.category()}")
        print("-" * 30)


class Store:

    def __init__(self):
        self.mobile_list = []

    def add_mobile(self, mobile):
        self.mobile_list.append(mobile)
        print(f"{mobile.brand} {mobile.model} added successfully.")

    def show_mobiles(self):
        print("\n------ Mobile Store ------")
        if len(self.mobile_list) == 0:
            print("No mobiles available.")
        else:
            for mobile in self.mobile_list:
                mobile.display()


# Main Program
store = Store()

store.add_mobile(Mobile("Samsung", "Galaxy S24", 74999))
store.add_mobile(Mobile("OnePlus", "Nord CE4", 25999))
store.add_mobile(Mobile("Redmi", "12C", 9999))

store.show_mobiles()

# output:
# Samsung Galaxy S24 added successfully.
# OnePlus Nord CE4 added successfully.
# Redmi 12C added successfully.

# ------ Mobile Store ------
# Brand    : Samsung
# Model    : Galaxy S24
# Price    : ₹74999
# Category : Premium
# ------------------------------
# Brand    : OnePlus
# Model    : Nord CE4
# Price    : ₹25999
# Category : Mid-range
# ------------------------------
# Brand    : Redmi
# Model    : 12C
# Price    : ₹9999
# Category : Budget
# ------------------------------
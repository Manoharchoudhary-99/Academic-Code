import csv
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python mobile.py mobiles.csv")
    exit()

filename = sys.argv[1]

folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, filename)

try:
    with open(file_path, "r", newline="") as file:
        mobiles = list(csv.DictReader(file))

    print("\nAll Mobile Records")
    print("-" * 40)

    for mobile in mobiles:
        print(mobile)

    print("-" * 40)

    brand = input("Enter Brand Name to search: ")

    found = False

    for mobile in mobiles:
        if mobile.get("Brand") and mobile["Brand"].lower() == brand.lower():
            print("\nMobile Found:")
            for key, value in mobile.items():
                print(f"{key}: {value}")
            found = True

    if not found:
        print("Mobile not found.")

except FileNotFoundError:
    print("Error: CSV file not found.")
import csv
import json
import os

folder = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(folder, "students.csv")
json_path = os.path.join(folder, "students.json")

if not os.path.exists(csv_path):
    print("Error: students.csv not found!")
    print("Please place students.csv in:", folder)
else:
    with open(csv_path, "r", newline="") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    with open(json_path, "w") as json_file:
        json.dump(data, json_file, indent=4)

    print("CSV data successfully converted to JSON!")
    print("Output file:", json_path)
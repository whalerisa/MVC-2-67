import csv
import os

CSV_FILE = "drivers.csv"

def create_csv_if_not_exists():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["license_number", "driver_type", "birthdate", "status"])

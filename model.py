import csv
from database import CSV_FILE

class Driver:
    def __init__(self, license_number, driver_type, birthdate, status="ปกติ"):
        self.license_number = license_number
        self.driver_type = driver_type
        self.birthdate = birthdate
        self.status = status

    def save_to_csv(self):
        """บันทึกข้อมูลลงไฟล์ CSV"""
        with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([self.license_number, self.driver_type, self.birthdate, self.status])

    @staticmethod
    def get_driver(license_number):
        """ดึงข้อมูลผู้ขับขี่จาก CSV"""
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["license_number"] == license_number:
                    return row
        return None

    @staticmethod
    def update_driver(license_number, new_status, new_driver_type):
        """อัปเดตสถานะและประเภทของผู้ขับขี่ใน CSV"""
        data = []
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row["license_number"] == license_number:
                    row["status"] = new_status
                    row["driver_type"] = new_driver_type
                data.append(row)

        # เขียนข้อมูลกลับไปที่ CSV
        with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["license_number", "driver_type", "birthdate", "status"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

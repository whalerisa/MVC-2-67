import random
from datetime import datetime
import csv
from collections import Counter
from database import CSV_FILE

def generate_driver_report():
    """อ่านข้อมูลจาก CSV และสร้างรายงานสรุป"""
    try:
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            driver_types = []
            driver_statuses = []

            for row in reader:
                driver_types.append(row["driver_type"])
                driver_statuses.append(row["status"])

            # นับจำนวนผู้ขับขี่ในแต่ละประเภทและสถานะ
            type_count = Counter(driver_types)
            status_count = Counter(driver_statuses)

            return type_count, status_count
    except FileNotFoundError:
        return {}, {}

def validate_license_number(license_number):
    """ตรวจสอบหมายเลขใบขับขี่ และคืนค่าพร้อมรายละเอียดข้อผิดพลาด"""
    if not license_number.isdigit():
        return False, "หมายเลขใบขับขี่ต้องเป็นตัวเลขเท่านั้น"
    if len(license_number) != 9:
        return False, "หมายเลขใบขับขี่ต้องมี 9 หลัก"
    if license_number[0] == "0":
        return False, "หมายเลขใบขับขี่ต้องไม่ขึ้นต้นด้วย 0"
    return True, None



def check_driver_status(driver):
    """คำนวณอายุและอัปเดตสถานะใบขับขี่"""
    birth_year = int(driver["birthdate"].split("/")[-1])
    current_year = datetime.now().year
    age = current_year - birth_year
    driver_type = driver["driver_type"]

    status_info = {
        "status": "ปกติ",
        "age": age,
        "show_test_button": False,
        "show_exam_buttons": False,
        "show_training_button": False,
        "complaints": 0
    }

    if driver_type == "บุคคลทั่วไป":
        if age >= 70:
            status_info["status"] = "หมดอายุ"
        elif age < 16:
            status_info["status"] = "ถูกระงับ"
        else:
            status_info["show_test_button"] = True

    elif driver_type == "มือใหม่":
        if age >= 50:
            status_info["status"] = "หมดอายุ"
        elif age < 16:
            status_info["status"] = "ถูกระงับ"
        else:
            status_info["show_exam_buttons"] = True

    elif driver_type == "คนขับรถสาธารณะ":
        if age >= 60:
            status_info["status"] = "หมดอายุ"
        elif age < 20:
            status_info["status"] = "ถูกระงับ"
        else:
            status_info["complaints"] = random.randint(0, 10)
            if status_info["complaints"] > 5:
                status_info["status"] = "ถูกระงับชั่วคราว"
                status_info["show_training_button"] = True
            status_info["show_test_button"] = True

    return status_info

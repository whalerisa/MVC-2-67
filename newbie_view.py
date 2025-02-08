import tkinter as tk
from controller import check_driver_status
from model import Driver

class NewbieDriverView:
    def __init__(self, root, driver):
        self.window = tk.Toplevel(root)
        self.window.title("หน้าสำหรับมือใหม่")
        self.window.geometry("350x250")

        self.driver = driver
        driver_info = check_driver_status(driver)

        # แสดงสถานะ
        label_status = tk.Label(self.window, text=f"สถานะ: {driver_info['status']}")
        label_status.pack(pady=10)

        # แสดงปุ่มสอบข้อเขียนและสอบปฏิบัติ ถ้าเงื่อนไขเข้าเกณฑ์
        if driver_info["show_exam_buttons"]:
            self.btn_writing_exam = tk.Button(self.window, text="สอบข้อเขียน", command=self.complete_writing_exam)
            self.btn_writing_exam.pack(pady=5)

            self.btn_practice_exam = tk.Button(self.window, text="สอบปฏิบัติ", command=self.complete_practice_exam)
            self.btn_practice_exam.pack(pady=5)

    def complete_writing_exam(self):
        self.btn_writing_exam.config(text="สิ้นสุดการสอบข้อเขียน", state=tk.DISABLED)
        self.check_promotion()

    def complete_practice_exam(self):
        self.btn_practice_exam.config(text="สิ้นสุดการสอบปฏิบัติ", state=tk.DISABLED)
        self.check_promotion()

    def check_promotion(self):
        """เลื่อนสถานะเป็นบุคคลทั่วไปเมื่อสอบครบ"""
        if self.btn_writing_exam["state"] == tk.DISABLED and self.btn_practice_exam["state"] == tk.DISABLED:
            self.driver["driver_type"] = "บุคคลทั่วไป"
            Driver.update_driver(self.driver["license_number"], "ปกติ", "บุคคลทั่วไป")

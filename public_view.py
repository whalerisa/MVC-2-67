import tkinter as tk
from controller import check_driver_status
from model import Driver

class PublicDriverView:
    def __init__(self, root, driver):
        self.window = tk.Toplevel(root)
        self.window.title("หน้าสำหรับคนขับรถสาธารณะ")
        self.window.geometry("350x250")

        self.driver = driver
        self.driver_info = check_driver_status(driver)

        self.status_label = tk.Label(self.window, text=f"สถานะ: {self.driver_info['status']}\nการร้องเรียน: {self.driver_info['complaints']} ครั้ง")
        self.status_label.pack(pady=10)

        self.training_completed = False

        # ถ้าการร้องเรียนเกิน 5 → แสดงปุ่ม "อบรม" และซ่อน "ทดสอบสมรรถนะ"
        if self.driver_info["show_training_button"]:
            self.btn_training = tk.Button(self.window, text="อบรม", command=self.complete_training)
            self.btn_training.pack(pady=5)

            self.btn_test = tk.Button(self.window, text="ทดสอบสมรรถนะ", command=self.start_test)
            self.btn_test.pack(pady=5)
            self.btn_test.pack_forget()  # ซ่อนปุ่มนี้ไว้ก่อน

        # ถ้าการร้องเรียน ≤ 5 → แสดงปุ่ม "ทดสอบสมรรถนะ" ทันที
        elif self.driver_info["show_test_button"]:
            self.btn_test = tk.Button(self.window, text="ทดสอบสมรรถนะ", command=self.start_test)
            self.btn_test.pack(pady=5)

    def complete_training(self):
        """เปลี่ยนปุ่ม 'อบรม' เป็น 'สิ้นสุดการอบรม' และเปลี่ยนสถานะกลับเป็น 'ปกติ'"""
        self.btn_training.config(text="สิ้นสุดการอบรม", state=tk.DISABLED)
        self.status_label.config(text="สถานะ: ปกติ\nการร้องเรียน: 0 ครั้ง")

        # อัปเดตสถานะในฐานข้อมูล
        Driver.update_driver(self.driver["license_number"], "ปกติ", "คนขับรถสาธารณะ")

        # แสดงปุ่ม "ทดสอบสมรรถนะ" หลังจากอบรมเสร็จ
        self.btn_test.pack(pady=5)

    def start_test(self):
        """เปลี่ยนปุ่ม 'ทดสอบสมรรถนะ' เป็น 'สิ้นสุดการทดสอบ'"""
        self.btn_test.config(text="สิ้นสุดการทดสอบ", state=tk.DISABLED)

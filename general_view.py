import tkinter as tk
from controller import check_driver_status

class GeneralDriverView:
    def __init__(self, root, driver):
        self.window = tk.Toplevel(root)
        self.window.title("หน้าสำหรับบุคคลทั่วไป")
        self.window.geometry("300x200")

        driver_info = check_driver_status(driver)

        # แสดงสถานะ
        label_status = tk.Label(self.window, text=f"สถานะ: {driver_info['status']}")
        label_status.pack(pady=10)

        # แสดงปุ่ม "ทดสอบสมรรถนะ" ถ้าเงื่อนไขเข้าเกณฑ์
        if driver_info["show_test_button"]:
            self.btn_test = tk.Button(self.window, text="ทดสอบสมรรถนะ", command=self.start_test)
            self.btn_test.pack(pady=10)

    def start_test(self):
        self.btn_test.config(text="สิ้นสุดการทดสอบ", state=tk.DISABLED)

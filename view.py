import tkinter as tk
from tkinter import messagebox
from controller import validate_license_number, check_driver_status
from model import Driver
from general_view import GeneralDriverView
from newbie_view import NewbieDriverView
from public_view import PublicDriverView
from report_view import ReportView

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("ระบบตรวจสอบใบขับขี่")
        self.root.geometry("400x200")

        self.label = tk.Label(root, text="กรอกหมายเลขใบขับขี่:")
        self.label.pack(pady=10)

        self.entry_license = tk.Entry(root, width=20)
        self.entry_license.pack(pady=5)

        self.btn_submit = tk.Button(self.root, text="ตรวจสอบ", command=self.check_driver)
        self.btn_submit.pack(pady=10)

        self.btn_report = tk.Button(self.root, text="ดูรายงาน", command=self.show_report)
        self.btn_report.pack(pady=10)
        # ตรวจสอบให้แน่ใจว่าผู้ใช้ป้อนเฉพาะตัวเลข
        self.entry_license.bind("<KeyRelease>", self.validate_input)

    def show_report(self):
        """แสดงหน้าต่างรายงาน"""
        ReportView(self.root)
    def validate_input(self, event):
        """ห้ามป้อนอักขระที่ไม่ใช่ตัวเลข"""
        current_text = self.entry_license.get()
        if not current_text.isdigit():
            self.entry_license.delete(0, tk.END)  # ลบข้อความที่ผิดพลาด
            messagebox.showwarning("ข้อผิดพลาด", "กรุณากรอกเฉพาะตัวเลขเท่านั้น")

    def check_driver(self):
        """ตรวจสอบข้อมูลใบขับขี่ และแสดงข้อผิดพลาดแบบละเอียด"""
        license_number = self.entry_license.get()
        is_valid, error_message = validate_license_number(license_number)

        if not is_valid:
            messagebox.showwarning("ข้อผิดพลาด", error_message)
            return

        driver = Driver.get_driver(license_number)
        if driver:
            driver_type = driver["driver_type"]

            # เปิด View ตามประเภทของผู้ขับขี่
            if driver_type == "บุคคลทั่วไป":
                GeneralDriverView(self.root, driver)
            elif driver_type == "มือใหม่":
                NewbieDriverView(self.root, driver)
            elif driver_type == "คนขับรถสาธารณะ":
                PublicDriverView(self.root, driver)
        else:
            messagebox.showwarning("ไม่พบข้อมูล", "หมายเลขใบขับขี่นี้ไม่มีในระบบ!")

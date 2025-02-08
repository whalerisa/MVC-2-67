import tkinter as tk
from controller import generate_driver_report

class ReportView:
    def __init__(self, root):
        self.window = tk.Toplevel(root)
        self.window.title("รายงานผู้ขับขี่")
        self.window.geometry("400x300")

        type_count, status_count = generate_driver_report()

        # รายงานจำนวนผู้ขับขี่แต่ละประเภท
        label_type = tk.Label(self.window, text="จำนวนผู้ขับขี่แต่ละประเภท:")
        label_type.pack(pady=5)
        for key, value in type_count.items():
            tk.Label(self.window, text=f"{key}: {value} คน").pack()

        # รายงานจำนวนผู้ขับขี่แต่ละสถานะ
        label_status = tk.Label(self.window, text="\nจำนวนผู้ขับขี่แต่ละสถานะ:")
        label_status.pack(pady=5)
        for key, value in status_count.items():
            tk.Label(self.window, text=f"{key}: {value} คน").pack()

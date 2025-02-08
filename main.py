import tkinter as tk
from view import LoginView
from database import create_csv_if_not_exists

if __name__ == "__main__":
    create_csv_if_not_exists()
    root = tk.Tk()
    app = LoginView(root)
    root.mainloop()


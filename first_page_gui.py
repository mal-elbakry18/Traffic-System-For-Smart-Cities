import tkinter as tk
from tkinter import messagebox
import time

class TrafficLightPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Cases")
        self.root.configure(bg='green')
        self.root.resizable(False, False)
        self.root.geometry("700x700")

        self.system_label = tk.Label(root, text="Traffic Light System", font=("Arial", 16, "bold"))
        self.system_label.grid(row=1, column=5, columnspan=5, padx=100, pady=50)

        self.case_1 = tk.Button(root, text="One-way crossroads", command=self.all_normal_case, height=2, width=15)
        self.case_2 = tk.Button(root, text="Four-way crossroads", command=self.all_unavailable_case, height=2, width=15)
        self.case_3 = tk.Button(root, text="Two-way crossroads", command=self.some_unavailable_case, height=2, width=15)
        middle_col = 5
        self.case_1.grid(row=2, column=middle_col, columnspan=5, padx=250, pady=50)
        self.case_2.grid(row=3, column=middle_col, columnspan=5, padx=250, pady=50)
        self.case_3.grid(row=4, column=middle_col, columnspan=5, padx=250, pady=50)

    def all_normal_case(self):
        self.open_new_window_1("One-way crossroads")

    def all_unavailable_case(self):
        self.open_new_window_2("Four-way crossroads")

    def some_unavailable_case(self):
        self.open_new_window_3("Two-way crossroads")

    def open_new_window_1(self, case):
        new_window = tk.Toplevel(self.root)
        new_window.title("New Window")
        new_window.configure(bg='white')
        new_window.resizable(False, False)
        new_window.geometry("300x200")

        new_window_label = tk.Label(new_window, text=f"Traffic Light Case: {case}", font=("Arial", 12, "bold"))
        new_window_label.pack(pady=10)

        new_window_close_button = tk.Button(new_window, text="Close", command=new_window.destroy, height=2, width=10)
        new_window_close_button.pack(pady=5)

def main():
    root = tk.Tk()
    TrafficLightPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
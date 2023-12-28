import tkinter as tk
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

        self.case_1_button = tk.Button(root, text="One-way crossroads", command=lambda: self.open_new_window("One-way crossroads"), height=2, width=15)
        self.case_2_button = tk.Button(root, text="Four-way crossroads", command=lambda: self.open_new_window("Four-way crossroads"), height=2, width=15)
        self.case_3_button = tk.Button(root, text="Two-way crossroads", command=lambda: self.open_new_window("Two-way crossroads"), height=2, width=15)

        middle_col = 5
        self.case_1_button.grid(row=2, column=middle_col, columnspan=4, padx=250, pady=50)
        self.case_2_button.grid(row=3, column=middle_col, columnspan=4, padx=250, pady=50)
        self.case_3_button.grid(row=4, column=middle_col, columnspan=4, padx=250, pady=50)

    def open_new_window(self, case):
        new_window = tk.Toplevel(self.root)
        new_window.title("Traffic Light")
        new_window.configure(bg='white')
        new_window.resizable(False, True)
        new_window.geometry("500x500")

        TrafficLight(new_window, case)

        new_window_close_button = tk.Button(new_window, text="Close", command=new_window.destroy, height=2, width=10)
        new_window_close_button.pack(pady=5)

    def open_new_window_1(self):
        self.open_new_window("One-way crossroads")

    def open_new_window_2(self):
        self.open_new_window("Four-way crossroads")

    def open_new_window_3(self):
        self.open_new_window("Two-way crossroads")

class TrafficLight:
    def __init__(self, master, case):
        self.master = master
        self.master.title("Traffic Light")

        self.canvas = tk.Canvas(self.master, width=150, height=300, bg="white")
        self.canvas.pack()

        if case == "One-way crossroads" or case == "Two-way crossroads":
            self.draw_traffic_light()
        elif case == "Four-way crossroads":
            self.draw_traffic_light_case_2()

        self.label = tk.Label(self.master, text="Value Of Timer", font=("Arial", 12))
        self.label.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start", command=self.turn_on_traffic_light)
        self.start_button.pack(pady=10)

        self.timer = 0
        self.update_label(self.timer)

    def draw_traffic_light(self):
        self.canvas.create_rectangle(50, 50, 100, 250, outline="black", width=3)
        self.red_light = self.canvas.create_oval(65, 70, 85, 90, fill="gray", outline="black")
        self.yellow_light = self.canvas.create_oval(65, 120, 85, 140, fill="gray", outline="black")
        self.green_light = self.canvas.create_oval(65, 170, 85, 190, fill="gray", outline="black")

    def draw_traffic_light_case_2(self):
        self.canvas.create_rectangle(50, 50, 100, 250, outline="black", width=3)
        self.forward_light = self.canvas.create_oval(65, 70, 85, 90, fill="gray", outline="black")
        self.canvas.create_text(75, 80, text="F", fill="black")
        self.right_light = self.canvas.create_oval(65, 120, 85, 140, fill="gray", outline="black")
        self.canvas.create_text(75, 130, text="R", fill="black")
        self.left_light = self.canvas.create_oval(65, 170, 85, 190, fill="gray", outline="black")

    def turn_on_traffic_light(self):
        self.timer = 0
        self.start_timer()

    def start_timer(self):
        self.change_light()

    def change_light(self):
        if self.timer % 300 == 0:
            self.update_red_light()
        elif self.timer % 300 == 30:
            self.update_yellow_light()
        elif self.timer % 300 == 35:  # Corrected timing for green light
            self.update_green_light()

        self.timer += 1
        self.update_label(self.timer)

        if self.timer < 300:
            self.master.after(1000, self.change_light)
        else:
            self.timer = 0

    def update_red_light(self):
        self.canvas.itemconfig(self.red_light, fill="red")

    def update_yellow_light(self):
        self.canvas.itemconfig(self.yellow_light, fill="yellow")

    def update_green_light(self):
        self.canvas.itemconfig(self.green_light, fill="green")

    def update_label(self, timer):
        self.label.config(text=timer)

def main():
    root = tk.Tk()
    TrafficLightPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()
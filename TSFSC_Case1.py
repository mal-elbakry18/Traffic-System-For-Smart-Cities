import tkinter as tk

class TrafficLight:
    def __init__(self, master):
        self.master = master
        self.master.title("Traffic Light")

        self.canvas = tk.Canvas(master, bg="white")
        self.canvas.pack()

        self.draw_traffic_light("red")

        self.current_color = "red"

        self.master.after(2000, self.switch_light)  # Auto-switch every 2000 milliseconds (2 seconds)

    def draw_traffic_light(self, color):
        self.canvas.delete("all")

        # Draw the traffic light body
        self.canvas.create_rectangle(50, 30, 80, 230, fill="gray", outline="gray")

        # Draw the lights
        self.canvas.create_oval(45, 30, 55, 70, fill="red" if color == "red" else "gray")
        self.canvas.create_oval(45, 90, 55, 130, fill="yellow" if color == "yellow" else "gray")
        self.canvas.create_oval(45, 150, 55, 190, fill="green" if color == "green" else "gray")

    def switch_light(self):
        if self.current_color == "red":
            self.current_color = "green"
        elif self.current_color == "green":
            self.current_color = "yellow"
        else:
            self.current_color = "red"

        self.draw_traffic_light(self.current_color)

        self.master.after(2000, self.switch_light)  # Auto-switch every 2000 milliseconds (2 seconds)

def main():
    root = tk.Tk()
    traffic_light = TrafficLight(root)
    root.mainloop()

if __name__ == "__main__":
    main()

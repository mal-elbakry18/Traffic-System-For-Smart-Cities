import time
import random
import C3gui
from PyQt5.QtWidgets import QApplication

class TrafficLight:
    # Constructor method
    def __init__(self, name, initial_state, widget):
        self.name = name
        self.state = initial_state
        self.car_count = 0
        self.time_in_state = 0
        self.widget = widget

    def change_state(self, next_state):
        self.state = next_state
        self.time_in_state = 0
        self.widget.state = next_state
        self.widget.update()

    # Method to simulate a car arriving at the light.
    def add_car(self):
        self.car_count += 1  # Increment the car count.

    # Method to simulate a car leaving the light.
    def remove_car(self):
        if self.car_count > 0:  # Only remove a car if there is at least one.
            self.car_count -= 1  # Decrement the car count.

# A class to represent an intersection of two traffic lights.
class Intersection:
    # Constructor method
    def __init__(self, light1, light2):
        self.light1 = light1  # The first traffic light.
        self.light2 = light2  # The second traffic light.
        self.state = 1  # The initial state of the intersection.

    # Method to operate the intersection for a certain number of seconds.
    def operate(self, time_limit):
        for _ in range(time_limit):

            # If a light is green, remove a car from its queue.
            if self.light1.state == "GREEN":
                self.light1.remove_car()
            if self.light2.state == "GREEN":
                self.light2.remove_car()

            # Increment the time each light has been in its current state.
            self.light1.time_in_state += 1
            self.light2.time_in_state += 1

            # Change the state of the lights and the intersection according to the rules of the finite state machine.
            if self.state == 1:
                if self.light2.car_count > 12 or self.light1.time_in_state >= 10:
                    self.light1.change_state("YELLOW")
                    self.state = 2
            elif self.state == 2:
                if self.light1.time_in_state >= 5:
                    self.light1.change_state("RED")
                    self.light2.change_state("GREEN")
                    self.state = 3
            elif self.state == 3:
                if self.light1.car_count > 12 or self.light2.time_in_state >= 10:
                    self.light2.change_state("YELLOW")
                    self.state = 4
            elif self.state == 4:
                if self.light2.time_in_state >= 5:
                    self.light2.change_state("RED")
                    self.light1.change_state("GREEN")
                    self.state = 1

            # Each loop run = one second
            time.sleep(1)

# Create two traffic lights with initial states.
# light1_widget = C3gui.TrafficLightWidget()
# light2_widget = C3gui.TrafficLightWidget()
# light1 = TrafficLight("Light 1", "GREEN", light1_widget)  # Pass the widget instance
# light2 = TrafficLight("Light 2", "RED", light2_widget)  # Pass the widget instance
#
# # Create an intersection with the two lights.
# intersection = Intersection(light1, light2)
#
# # Create and run the GUI.
# app = QApplication([])
# gui = C3gui.TrafficLightGUI(intersection)
# gui.show()
# app.exec_()

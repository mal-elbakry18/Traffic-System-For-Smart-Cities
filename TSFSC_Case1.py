import time


class TrafficLight:
    def __init__(self):
        self.states = {'Red': RedState(), 'Green': GreenState(), 'Yellow': YellowState()}
        self.current_state = self.states['Red']
        self.timer = 0
        self.number_of_cars = 0
        self.number_of_passenger = 0

    def set_state(self, state):
        self.current_state = state
        self.timer = 0  # Reset the timer when the state changes
        print(f"Current state: {self.current_state} "
              f"| Cars waiting: {self.num_cars_waiting} "
              f"| People waiting: {self.num_people_waiting}")
    def stay_in_red(self):
       



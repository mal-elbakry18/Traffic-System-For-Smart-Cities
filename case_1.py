import time
import tkinter as tk
import first_page_gui as gui

# Diagram of the road
# ____________________--------______________>
# ____________________--------______________>
# ____________________--------______________>
# ____________________--------______________>
# <____________________--------______________
# <____________________--------______________
# <____________________--------______________
# <____________________--------______________


# Global variables for the class check states:
state_list = ["RED", "YELLOW", "GREEN"]


# Function to check the states by time and by number of cars (in case of red)
# and number of people(in case of green)
class Check_states:

    def __init__(self):
        self.number_of_cars = 0
        self.number_of_people = 0
        self.cars_passed = 12
        self.tr = 0
        self.ty = 0
        self.tg = 0
        self.p_state = state_list[0]
        self.next_state = state_list[1]
        self.current_state = state_list[0]

    def check_red_state(self, tr, number_of_cars):
        if tr == 30 and number_of_cars > 0:
            self.tr = 0
            return "YELLOW"
        elif tr == 30 and number_of_cars == 0:
            self.tr = 0
            return "RED"
        else:
            return "RED"

    # keep record of the previous state

    def check_yellow_state(self, ty, p_state):
        if ty == 5 and p_state == "RED":
            self.ty = 0
            return "GREEN"
        elif ty == 5 and p_state == "GREEN":
            self.ty = 0
            return "RED"
        else:
            return "YELLOW"

    # Check for the number of cars passed

    def check_green_state(self, tg, number_of_people):
        if tg == 30 and number_of_people > 0:
            self.tg = 0
            return "YELLOW"
        elif tg == 30 and number_of_people == 0:
            self.tg = 0
            return "YELLOW"
        else:
            return "GREEN"

    def get_current_state(self):
        return self.current_state

    def get_timer(self):
        if self.current_state == "RED":
            return self.tr
        elif self.current_state == "YELLOW":
            return self.ty
        elif self.current_state == "GREEN":
            return self.tg


'''
    state_dict = {state_list[0]: check_red_state(tr, number_of_cars),
                  state_list[1]: check_yellow_state(ty, p_state),
                  state_list[2]: check_green_state(tg, number_of_people, cars_passed)}

'''


class RED_STATE(Check_states):
    def switch(self, check_states_instances):
        check_states_instances.p_state = state_list[1]
        check_states_instances.current_state = state_list[0]


class YELLOW_STATE(Check_states):
    def switch(self, check_states_instances):
        if check_states_instances.current_state == "RED":
            check_states_instances.next_state = state_list[2]
            check_states_instances.p_state = state_list[0]
            check_states_instances.current_state = state_list[1]

        elif check_states_instances.current_state == "GREEN":
            check_states_instances.p_state = state_list[2]
            check_states_instances.current_state = state_list[1]
            check_states_instances.next_state = state_list[0]


class GREEN_STATE(Check_states):
    def switch(self, check_states_instances):
        check_states_instances.p_state = state_list[1]
        check_states_instances.current_state = state_list[2]


class Return:
    def first_loop(self, state):
        return state


def main():
    nb_of_cars = 20
    nb_of_people = 10
    Check_states_obj = Check_states()
    Red_state_instances = RED_STATE()
    Yellow_state_instances = YELLOW_STATE()
    Green_state_instances = GREEN_STATE()
    return_obj = Return()

    while True:
        for i in range(30):
            Check_states_obj.check_red_state(Check_states_obj.tr, nb_of_cars)
            Check_states_obj.tr += 1
            print(f"Current time is {Check_states_obj.tr}")
            time.sleep(1)
            if nb_of_cars > 12 or nb_of_cars < 12:
                if nb_of_cars != 0:
                    nb_of_cars -= 1
                else:
                    nb_of_cars = 0

            if Check_states_obj.tr == 0 and nb_of_cars == 0:
                i = 0
            state = Check_states_obj.current_state
            return_obj.first_loop(state)

            print(f"{Check_states_obj.current_state}")
            print(f"Number of cars: {nb_of_cars}")
            #print("out of loop 1 ")
        Yellow_state_instances.switch(Check_states_obj)
        print(f"Previous state is:{Check_states_obj.p_state}")
        print(f"Current state is:{Check_states_obj.current_state}")

        for j in range(5):
            Check_states_obj.check_yellow_state(Check_states_obj.ty, Check_states_obj.p_state)
            Check_states_obj.ty += 1
            print(f"Current time is {Check_states_obj.ty}")
            time.sleep(1)
        #print("out of loop 2")
        Green_state_instances.switch(Check_states_obj)
        print(f"Current state is: {Check_states_obj.current_state}")
        print(f"Previous state is:{Check_states_obj.p_state}")

        for k in range(30):

            Check_states_obj.check_green_state(Check_states_obj.tg, nb_of_people)
            Check_states_obj.tg += 1
            print(f"Current time is {Check_states_obj.tg}")
            time.sleep(1)
            if nb_of_people >= 12:
                nb_of_people -= 1

        #print("out of loop 3")

        Yellow_state_instances.switch(Check_states_obj)
        print(f"Current state is:{Check_states_obj.current_state}")
        print(f"Previous state is:{Check_states_obj.p_state}")

        for j in range(5):
            Check_states_obj.check_yellow_state(Check_states_obj.ty, Check_states_obj.p_state)
            Check_states_obj.ty += 1
            print(f"Current time is {Check_states_obj.ty}")
            time.sleep(1)
        print("out of loop 4")

        Red_state_instances.switch(Check_states_obj)
        print(f"Current state is: {Check_states_obj.current_state}")
        print(f"Previous state is:{Check_states_obj.p_state}")

if __name__ == '__main__':
   main()

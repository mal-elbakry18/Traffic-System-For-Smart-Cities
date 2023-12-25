import time

# Global variables for the class check states:
'''number_of_cars = 0
number_of_people = 0
cars_passed = 12'''
state_list = ["RED", "YELLOW", "GREEN"]
'''tr = 0
tg = 0
ty = 3
p_state = state_list[0]'''


class Check_states():

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
            # check_red_state(tr, number_of_cars)
            return "RED"
        else:
            return "RED"

    # keep record of the previous state

    def check_yellow_state(self, ty, p_state):
        if ty == 3 and p_state == "RED":
            self.ty = 0
            return "GREEN"
        elif ty == 3 and p_state == "GREEN":
            self.ty = 0
            return "RED"
        else:
            return "YELLOW"

    # Check for the number of cars passed

    def check_green_state(self, tg, number_of_people, cars_passed):
        if tg == 50 and number_of_people > 0:
            self.tg = 0
            return "YELLOW"
        elif (tg == 50 and number_of_people == 0) or cars_passed == 20:
            self.tg = 0
            return "YELLOW"
        else:
            return "GREEN"


# def transtion_of_states(self):

'''
    state_dict = {state_list[0]: check_red_state(tr, number_of_cars),
                  state_list[1]: check_yellow_state(ty, p_state),
                  state_list[2]: check_green_state(tg, number_of_people, cars_passed)}

'''


class RED_STATE(Check_states):
    def switch(self, check_states_instances):
        check_states_instances.p_states = state_list[1]
        check_states_instances.current_state = state_list[0]


class YELLOW_STATE(Check_states):
    def switch(self, check_states_instances):
        check_states_instances.current_state = state_list[1]

        if check_states_instances.p_states == "RED":
            check_states_instances.next_state = state_list[2]

        elif check_states_instances.p_states == "GREEN":
            check_states_instances.next_state = state_list[0]


class GREEN_STATE(Check_states):
    def switch(self, check_states_instances):
        check_states_instances.p_states = state_list[1]
        check_states_instances.current_state = state_list[2]




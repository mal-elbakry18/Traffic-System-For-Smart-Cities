import time


# check if we should stay in the red state

def reset_tr():
    tr = 0
    # return tr


def check_red_state(tr, number_of_cars):
    if tr == 30 and number_of_cars > 0:
        return "YELLOW"
    elif tr == 30 and number_of_cars == 0:
        reset_tr()
        # check_red_state(tr, number_of_cars)
        return "RED"
    else:
        return "RED"


# keep record of the previous state


def check_yellow_state(ty, p_state):
    if ty == 3 and p_state == "RED":
        return "GREEN"
    elif ty == 3 and p_state == "GREEN":
        return "RED"
    else:
        return "YELLOW"

# Check for the number of cars passed


def check_green_state(tg, number_of_people, cars_passed):
    if tg == 50 and number_of_people > 0:
        return "YELLOW"
    elif (tg == 50 and number_of_people == 0) or cars_passed == 20:
        return "YELLOW"
    else:
        return "GREEN"

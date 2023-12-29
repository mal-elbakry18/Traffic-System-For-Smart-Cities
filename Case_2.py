import time

# This case is
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#            ____ |   E     | F     |  G    | H     |
#            |  |
# _________________                                       ____________________
#                   d                                        e
# _________________                                       ____________________
#                   c                                        f
# _________________                                       ____________________
#                   b                                        g
# _________________                                       ____________________
#                   a                                        h
# _________________                                       ____________________
#                 |   A     |   B   |   C   |  D    |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |
#                 |         |       |       |       |

# State 1:      |   State 2:    |   State 3:    |   State 4:
# a -->Green    |   B -->Green  |   e-->Green   |   E -->Green
# b -->Green    |   C -->Green  |   g-->Green   |   F-->Green
# c -->Green    |   D -->Green  |   f-->Green   |   G--> Green
# E -->Green    |   a-->Green   |   D-->Green   |   e-->Green

state_list = ["RED", "YELLOW", "GREEN"]


class Lane():
    def __init__(self):
        self.nb_of_cars = 0
        self.time = 0
        self.state = state_list[0]
        self.tr = 0
        self.ty = 0
        self.tg = 0
        self.p_state = state_list[0]
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

    def check_yellow_state(self, ty, p_state):
        if ty == 5 and p_state == "RED":
            self.ty = 0
            return "GREEN"
        elif ty == 5 and p_state == "GREEN":
            self.ty = 0
            return "RED"

        else:
            return "YELLOW"

    def check_green_state(self, tg):
        if tg == 30:
            self.tg = 0
            return "YELLOW"
        elif tg == 30:
            self.tg = 0
            return "YELLOW"
        else:
            return "GREEN"

    def check_nb_of_cars(self):
        return self.nb_of_cars


class RED_STATE(Lane):
    def switch(self, lane_instances):
        lane_instances.p_state = state_list[1]
        lane_instances.current_state = state_list[0]


class YELLOW_STATE(Lane):
    def switch(self, lane_instances):
        for lane in lane_instances:
            if lane.current_state == "RED":
                lane.p_state = state_list[0]
                lane.current_state = state_list[1]

            elif lane.current_state == "GREEN":
                lane.p_state = state_list[2]
                lane.current_state = state_list[1]


class GREEN_STATE(Lane):
    def switch(self, lane_instances):
        lane_instances.p_state = state_list[1]  # Yellow
        lane_instances.current_state = state_list[2]  # Green


class Initialize_lane:
    # Create obj from the lanes and initialize
    def __init__(self):
        self.lane_a = Lane()
        self.lane_b = Lane()
        self.lane_c = Lane()
        self.lane_d = Lane()
        self.lane_e = Lane()
        self.lane_f = Lane()
        self.lane_g = Lane()
        self.lane_h = Lane()
        self.lane_A = Lane()
        self.lane_B = Lane()
        self.lane_C = Lane()
        self.lane_D = Lane()
        self.lane_E = Lane()
        self.lane_F = Lane()
        self.lane_G = Lane()
        self.lane_H = Lane()

        self.Red_state_obj = RED_STATE()
        self.Yellow_state_obj = YELLOW_STATE()
        self.Green_state_obj = GREEN_STATE()

    def state_1(self):
        # All the lanes that are green
        self.Green_state_obj.switch(self.lane_a)
        self.Green_state_obj.switch(self.lane_b)
        self.Green_state_obj.switch(self.lane_c)
        self.Green_state_obj.switch(self.lane_E)

        # All the lanes that are red from lane 1
        self.Red_state_obj.switch(self.lane_d)
        self.Red_state_obj.switch(self.lane_e)
        self.Red_state_obj.switch(self.lane_f)
        self.Red_state_obj.switch(self.lane_g)
        self.Red_state_obj.switch(self.lane_h)

        # All the lanes that are red from lane 2
        self.Red_state_obj.switch(self.lane_A)
        self.Red_state_obj.switch(self.lane_B)
        self.Red_state_obj.switch(self.lane_C)
        self.Red_state_obj.switch(self.lane_D)
        self.Red_state_obj.switch(self.lane_F)
        self.Red_state_obj.switch(self.lane_G)
        self.Red_state_obj.switch(self.lane_H)

        return "STATE_1"

    def state_1_yellow(self):
        # Switch to yellow after red
        red_lane = [self.lane_a, self.lane_b, self.lane_c,
                    self.lane_E]
        self.Yellow_state_obj.switch(red_lane)
        # Switch from green to yellow
        green_lane = [self.lane_d, self.lane_e, self.lane_f, self.lane_g, self.lane_h, self.lane_A,
                      self.lane_B, self.lane_C, self.lane_D, self.lane_F, self.lane_G, self.lane_H]
        self.Yellow_state_obj.switch(green_lane)

    def state_2(self):
        # All the lanes that are green
        self.Green_state_obj.switch(self.lane_B)
        self.Green_state_obj.switch(self.lane_C)
        self.Green_state_obj.switch(self.lane_D)
        self.Green_state_obj.switch(self.lane_a)

        # All the lanes that are red from lane 2
        self.Red_state_obj.switch(self.lane_A)
        self.Red_state_obj.switch(self.lane_E)
        self.Red_state_obj.switch(self.lane_F)
        self.Red_state_obj.switch(self.lane_G)
        self.Red_state_obj.switch(self.lane_H)

        # All the lanes that are red from lane 1
        self.Red_state_obj.switch(self.lane_b)
        self.Red_state_obj.switch(self.lane_c)
        self.Red_state_obj.switch(self.lane_d)
        self.Red_state_obj.switch(self.lane_e)
        self.Red_state_obj.switch(self.lane_f)
        self.Red_state_obj.switch(self.lane_g)
        self.Red_state_obj.switch(self.lane_h)

        return "STATE_2"

    def state_2_yellow(self):
        # Switch to yellow after red
        red_lane = [self.lane_B, self.lane_C, self.lane_D,
                    self.lane_a]
        self.Yellow_state_obj.switch(red_lane)
        # Switch from green to yellow
        green_lane = [self.lane_A, self.lane_E, self.lane_F, self.lane_G, self.lane_H, self.lane_b,
                      self.lane_c, self.lane_d, self.lane_e, self.lane_f, self.lane_g, self.lane_h]
        self.Yellow_state_obj.switch(green_lane)

    def state_3(self):
        # All the lanes that are green
        self.Green_state_obj.switch(self.lane_D)
        self.Green_state_obj.switch(self.lane_e)
        self.Green_state_obj.switch(self.lane_g)
        self.Green_state_obj.switch(self.lane_f)

        # All the lanes that are red from lane 1
        self.Red_state_obj.switch(self.lane_b)
        self.Red_state_obj.switch(self.lane_c)
        self.Red_state_obj.switch(self.lane_d)
        self.Red_state_obj.switch(self.lane_h)
        self.Red_state_obj.switch(self.lane_E)

        # All the lanes that are red from lane 2
        self.Red_state_obj.switch(self.lane_A)
        self.Red_state_obj.switch(self.lane_B)
        self.Red_state_obj.switch(self.lane_C)
        self.Red_state_obj.switch(self.lane_a)
        self.Red_state_obj.switch(self.lane_F)
        self.Red_state_obj.switch(self.lane_G)
        self.Red_state_obj.switch(self.lane_H)

        return "STATE_3"

    def state_3_yellow(self):
        # Switch to yellow after red
        red_lane = [self.lane_D, self.lane_e, self.lane_g,
                    self.lane_f]
        self.Yellow_state_obj.switch(red_lane)
        # Switch from green to yellow
        green_lane = [self.lane_b, self.lane_c, self.lane_d, self.lane_h, self.lane_E, self.lane_A,
                      self.lane_B, self.lane_C, self.lane_a, self.lane_F, self.lane_G, self.lane_H]
        self.Yellow_state_obj.switch(green_lane)

    def state_4(self):
        # All the lanes that are green
        self.Green_state_obj.switch(self.lane_E)
        self.Green_state_obj.switch(self.lane_F)
        self.Green_state_obj.switch(self.lane_G)
        self.Green_state_obj.switch(self.lane_e)

        # All the lanes that are red from lane 1
        self.Red_state_obj.switch(self.lane_a)
        self.Red_state_obj.switch(self.lane_b)
        self.Red_state_obj.switch(self.lane_c)
        self.Red_state_obj.switch(self.lane_d)
        self.Red_state_obj.switch(self.lane_f)
        self.Red_state_obj.switch(self.lane_g)
        self.Red_state_obj.switch(self.lane_h)

        # All the lanes that are red from lane 2
        self.Red_state_obj.switch(self.lane_A)
        self.Red_state_obj.switch(self.lane_B)
        self.Red_state_obj.switch(self.lane_C)
        self.Red_state_obj.switch(self.lane_D)
        self.Red_state_obj.switch(self.lane_H)

        return "STATE_4"

    def state_4_yellow(self):
        # Switch to yellow after red
        red_lane = [self.lane_E, self.lane_F, self.lane_G,
                    self.lane_e]
        self.Yellow_state_obj.switch(red_lane)
        # Switch from green to yellow
        green_lane = [self.lane_a, self.lane_b, self.lane_c, self.lane_d, self.lane_f, self.lane_g,
                      self.lane_h, self.lane_C, self.lane_D, self.lane_A, self.lane_B, self.lane_H]
        self.Yellow_state_obj.switch(green_lane)


def main():
    init_lanes = Initialize_lane()

    nb_of_cars = 20
    while True:
        init_lanes.state_1()
        lanes_1_g = [init_lanes.lane_a, init_lanes.lane_b, init_lanes.lane_c, init_lanes.lane_E]
        lane_1_r = []
        for i in range(30):
            for lane in lanes_1_g:
                lane.check_green_state(lane.tg)
                lane.tg += 1
                print("-----------------------------------------------")
                print(f"{lane.current_state}")
            print(f"Current time: {lane.tg}")
            time.sleep(1)
        init_lanes.state_1_yellow()
        lanes = [init_lanes.lane_a, init_lanes.lane_b, init_lanes.lane_c, init_lanes.lane_E]
        for j in range(3):
            for lane in lanes:
                lane.check_yellow_state(lane.ty, lane.current_state)
                lane.ty += 1
                print("-----------------------------------------------")
                print(f"lane current state is: {lane.current_state}")

            print(f"Current time: {lane.ty}")
            time.sleep(1)

        lanes_2_G = [init_lanes.lane_a, init_lanes.lane_B, init_lanes.lane_C, init_lanes.lane_D]
        init_lanes.state_2()
        for i in range(30):
            for lane in lanes_2_G:
                lane.check_green_state(lane.tg)
                lane.tg += 1
                print("-----------------------------------------------")
                print(f"{lane.current_state}")
            print(f"Current time: {lane.tg}")
            time.sleep(1)
        init_lanes.state_2_yellow()
        lanes_2_y = [init_lanes.lane_a, init_lanes.lane_B, init_lanes.lane_C, init_lanes.lane_D]
        for j in range(3):
            for lane in lanes_2_y:
                lane.check_yellow_state(lane.ty, lane.p_state)
                lane.ty += 1
                print("-----------------------------------------------")
                print(f"lane current state is: {lane.current_state}")

            print(f"Current time: {lane.ty}")
            time.sleep(1)
'''    init_lanes.state_2()

    init_lanes.state_3()


    init_lanes.state_4()
    init_lanes.lane_a.check_red_state(init_lanes.lane_a.tr,20)
    init_lanes.lane_a.tg += 1
    print(f"{init_lanes.lane_a.current_state}")
'''

'''red_lanes_1 = [self.lane_d, self.lane_e, self.lane_f, self.lane_g, self.lane_h, self.lane_A, self.lane_B, self.lane_C,
                   self.lane_D,
                   self.lane_F, self.lane_G, self.lane_H]
    red_lanes_1[0].current_state = state_list[2]
    state = "GREEN"
    while state == "RED":
        print("in once")
        for lane in red_lanes_1:
            state = self.Ged_state_obj.check_ged_state(lane.tg)
            lane.tr += 1
            print(f"{lane} is in RED state.")
    print("Out of loop ")'''

''' for i in range(30):
        init_lanes.lane_a.check_red_state(init_lanes.lane_a.tr, nb_of_cars)
        init_lanes.lane_b.check_red_state(init_lanes.lane_b.tr, nb_of_cars)
        init_lanes.lane_c.check_red_state(init_lanes.lane_c.tr, nb_of_cars)
        init_lanes.lane_E.check_red_state(init_lanes.lane_E.tr, nb_of_cars)'''

if __name__ == '__main__':
    main()

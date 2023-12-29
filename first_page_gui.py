import tkinter as tk
import case_1
import time
import networkx as nx
import matplotlib.pyplot as plt


def create_nfa_diagram(states, alphabet, transition_function, start_state, accept_states, accept_style='filled',
                       accept_color='lightblue'):
    G = nx.DiGraph()

    # Add states to the graph
    for state in states:
        G.add_node(state)

    # Add edges for each symbol in the alphabet
    for symbol in alphabet:
        for state in states:
            next_state = transition_function.get((state, symbol))
            if next_state is not None:
                label = f"{symbol}\n{next_state}"
                G.add_edge(state, next_state, label=label)

    # Add start and accept states with styling
    G.add_node(start_state, shape='doublecircle')
    for accept_state in accept_states:
        G.nodes[accept_state]['style'] = accept_style
        G.nodes[accept_state]['fillcolor'] = accept_color

    return G


class TrafficLightPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Traffic Light Cases")
        self.root.configure(bg='green')
        self.root.resizable(False, False)
        self.root.geometry("700x700")

        self.system_label = tk.Label(root, text="Traffic Light System", font=("Arial", 16, "bold"))
        self.system_label.grid(row=1, column=5, columnspan=5, padx=100, pady=50)

        self.case_1_button = tk.Button(root, text="One-way crossroads", command=self.open_new_window_1, height=2,
                                       width=15)
        self.case_2_button = tk.Button(root, text="Four-way crossroads", command=self.open_new_window_2, height=2,
                                       width=15)
        self.case_3_button = tk.Button(root, text="Two-way crossroads", command=self.open_new_window_3, height=2,
                                       width=15)
        self.case_1_button_NFA = tk.Button(root, text="One-way crossroads", command=self.open_nfa_1, height=2, width=15)
        self.case_2_button_NFA = tk.Button(root, text="Four-way crossroads", command=self.open_nfa_2, height=2,
                                           width=15)
        self.case_3_button_NFA = tk.Button(root, text="Two-way crossroads", command=self.open_nfa_3, height=2, width=15)

        middle_col = 5
        self.case_1_button.grid(row=2, column=middle_col, columnspan=4, padx=250, pady=50)
        self.case_2_button.grid(row=3, column=middle_col, columnspan=4, padx=250, pady=50)
        self.case_3_button.grid(row=4, column=middle_col, columnspan=4, padx=250, pady=50)
        self.case_1_button_NFA.grid(row=2, column=7, columnspan=4, padx=250, pady=50)
        self.case_2_button_NFA.grid(row=3, column=7, columnspan=4, padx=250, pady=50)
        self.case_3_button_NFA.grid(row=4, column=7, columnspan=4, padx=250, pady=50)

    def open_new_window_1(self):
        self.open_new_window("One-way crossroads")

    def open_new_window_2(self):
        self.open_new_window_2("Four-way crossroads")

    def open_new_window_3(self):
        self.open_new_window_3()

    def open_nfa_1(self):
        # TrafficLight(new_window, case)
        states = ['G', 'Y', 'R']
        alphabet = ['T=30 & NC>0', 'T<30', 'T=5', 'T<5', 'T=30 & NC=0']
        transition_function = {
            ('R', 'T<30'): 'R', ('R', 'T=30 & NC=0'): 'R', ('R', 'T=30 & NC>0'): 'Y',
            ('Y', 'T<5'): 'Y', ('Y', 'T=5'): 'G', ('G', 'T<30'): 'G', ('G', 'T=30 & NP>0'): 'Y'
        }

        start_state = 'R'
        accept_states = {'G', 'R', }
        G = create_nfa_diagram(states, alphabet, transition_function, start_state, accept_states)

        # Display the diagram with edge labels
        pos = nx.spring_layout(G)  # You may choose a different layout

        # Adjust figure size and font size
        plt.figure(figsize=(15, 8))
        font_size = 12

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, font_size=font_size, node_size=500, node_color='skyblue', font_color='black')

        # Draw edge labels
        labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=7)

        # Show the plot
        plt.show()

    def open_nfa_2(self):
        states = ['1', '2', 'y', '3', '4']
        alphabet = ['T=30', 'T<30', 'T=5', 'T<5']
        transition_function = {('1', 'T<30'): '1', ('1', 'T=30'): 'Y',
                               ('Y', 'T<5'): 'Y', ('Y', 'T=5'): '1',
                               ('Y', 'T=5'): '2', ('Y', 'T=5'): '3',
                               ('Y', 'T=5'): '4', ('2', 'T<30'): '2',
                               ('2', 'T=30'): 'Y', ('3', 'T<30'): '3',
                               ('3', 'T=30'): 'Y', ('4', 'T<30'): '4',
                               ('4', 'T=30'): 'Y'}
        start_state = '1'
        accept_states = {'1', '2', '3', '4'}
        G = create_nfa_diagram(states, alphabet, transition_function, start_state, accept_states)

        # Display the diagram with edge labels
        pos = nx.spring_layout(G)  # You may choose a different layout

        # Adjust figure size and font size
        plt.figure(figsize=(15, 8))
        font_size = 12

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, font_size=font_size, node_size=700, node_color='skyblue', font_color='black')

        # Draw edge labels
        labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6)

        # Show the plot
        plt.show()

    def open_nfa_3(self):
        states = ['G1R2', 'Y1R2', 'R1G2', 'R1Y2']
        alphabet = ['NC_2>12 || T >50', 'T=5', 'T>50 || NC_1>12']
        transition_function = {('G1R2', 'NC_2>12 || T >50'): 'Y1R2',
                               ('Y1R2', 'T=5'): 'R1G2',
                               ('R1G2', 'T>50 || NC_1>12'): 'R1Y2',
                               ('R1Y2', 'T=5'): 'G1R2'}
        start_state = 'R1G1'
        accept_states = {'R1G1', 'G1R2'}
        G = create_nfa_diagram(states, alphabet, transition_function, start_state, accept_states)

        # Display the diagram with edge labels
        pos = nx.spring_layout(G)  # You may choose a different layout

        # Adjust figure size and font size
        plt.figure(figsize=(15, 8))
        font_size = 12

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, font_size=font_size, node_size=1000, node_color='skyblue', font_color='black')

        # Draw edge labels
        labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6)

        # Show the plot
        plt.show()

    def open_new_window(self, case):
        new_window = tk.Toplevel(self.root)
        new_window.title("New Window")
        new_window.configure(bg='white')
        new_window.resizable(False, True)
        new_window.geometry("500x500")

        TrafficLight(new_window, case)

        new_window_close_button = tk.Button(new_window, text="Close", command=new_window.destroy, height=2, width=10)
        new_window_close_button.pack(pady=5)

    def open_new_window_2(self, case):
        new_window = tk.Toplevel(self.root)
        new_window.title("New Window")
        new_window.configure(bg='white')
        new_window.resizable(False, True)
        new_window.geometry("500x500")

        TrafficLight(new_window, case)

        new_window_close_button = tk.Button(new_window, text="Close", command=new_window.destroy, height=2, width=10)
        new_window_close_button.pack(pady=5)

    def open_new_window_3(self):
        # TrafficLight(new_window, case)
        states = ['1', '2', 'y', '3', '4']
        alphabet = ['T=30', 'T<30', 'T=3', 'T<3']
        transition_function = {('1', 'T<30'): '1', ('1', 'T=30'): 'Y',
                               ('Y', 'T<3'): 'Y', ('Y', 'T=3'): '1',
                               ('Y', 'T=3'): '2', ('Y', 'T=3'): '3',
                               ('Y', 'T=3'): '4', ('2', 'T<30'): '2',
                               ('2', 'T=30'): 'Y', ('3', 'T<30'): '3',
                               ('3', 'T=30'): 'Y', ('4', 'T<30'): '4',
                               ('4', 'T=30'): 'Y'}
        start_state = '1'
        accept_states = {'1', '2', '3', '4'}
        G = create_nfa_diagram(states, alphabet, transition_function, start_state, accept_states)

        # Display the diagram with edge labels
        pos = nx.spring_layout(G)  # You may choose a different layout

        # Adjust figure size and font size
        plt.figure(figsize=(15, 8))
        font_size = 12

        # Draw nodes and edges
        nx.draw(G, pos, with_labels=True, font_size=font_size, node_size=700, node_color='skyblue', font_color='black')

        # Draw edge labels
        labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=6)

        # Show the plot
        plt.show()


class TrafficLight:
    def __init__(self, master, case):
        self.master = master
        self.master.title("Traffic Light")

        # Canvas to draw the traffic light
        self.canvas = tk.Canvas(self.master, width=150, height=300, bg="white")
        self.canvas.pack()

        # Draw the traffic light based on the case
        if case == "One-way crossroads":
            self.draw_traffic_light()
        elif case == "Four-way crossroads":
            self.draw_traffic_light_case_2()

        self.label = tk.Label(self.master, text="Value Of Timer", font=("Arial", 12))
        self.label.pack(pady=10)

        # Buttons to control the traffic light
        self.start_button = tk.Button(self.master, text="Start", command=self.turn_on_traffic_light)
        self.start_button.pack(pady=10)

    def draw_traffic_light(self):
        # Draw the outer rectangle
        self.canvas.create_rectangle(50, 50, 100, 250, outline="black", width=3)

        # Draw the red light
        self.red_light = self.canvas.create_oval(65, 70, 85, 90, fill="gray", outline="black")

        # Draw the yellow light
        self.yellow_light = self.canvas.create_oval(65, 120, 85, 140, fill="gray", outline="black")

        # Draw the green light
        self.green_light = self.canvas.create_oval(65, 170, 85, 190, fill="gray", outline="black")

    def draw_traffic_light_case_2(self):
        # Draw the outer rectangle
        self.canvas.create_rectangle(50, 50, 100, 250, outline="black", width=3)

        # Draw the forward light
        self.forward_light = self.canvas.create_oval(65, 70, 85, 90, fill="gray", outline="black")
        self.canvas.create_text(75, 80, text="F", fill="black")

        # Draw the right light
        self.right_light = self.canvas.create_oval(65, 120, 85, 140, fill="gray", outline="black")
        self.canvas.create_text(75, 130, text="R", fill="black")

        # Draw the left light
        self.left_light = self.canvas.create_oval(65, 170, 85, 190, fill="gray", outline="black")
        self.canvas.create_text(75, 180, text="L", fill="black")

    def turn_on_traffic_light(self):
        Case_1_obj = case_1
        Check_states_obj = Case_1_obj.Check_states()
        states_obj = Check_states_obj.get_current_state()
        return_state = states_obj
        nb_of_cars = 20
        nb_of_people = 10

        Red_state_instances = Case_1_obj.RED_STATE()
        Yellow_state_instances = Case_1_obj.YELLOW_STATE()
        Green_state_instances = Case_1_obj.GREEN_STATE()

        def update_red_light():
            nonlocal nb_of_cars
            Check_states_obj.check_red_state(Check_states_obj.tr, 20)
            nb_of_cars = max(0, nb_of_cars - 1)

        def update_yellow_light():
            Check_states_obj.check_yellow_state(Check_states_obj.ty, Check_states_obj.p_state)

        def update_green_light():
            nonlocal nb_of_people
            Green_state_instances.switch(Check_states_obj)
            Check_states_obj.check_green_state(Check_states_obj.tg, 5)
            nb_of_people = max(0, nb_of_people - 1)

        def update_traffic_light():
            nonlocal return_state

            update_red_light()
            update_yellow_light()
            update_green_light()

            if return_state == "RED":
                self.canvas.itemconfig(self.red_light, fill="red")
            elif return_state == "GREEN":
                self.canvas.itemconfig(self.green_light, fill="green")
            elif return_state == "YELLOW":
                self.canvas.itemconfig(self.yellow_light, fill="yellow")

            # Update label
            timer = max(Check_states_obj.tr, Check_states_obj.ty, Check_states_obj.tg)
            self.label.config(text=timer)

            # Schedule the next update after 1000 milliseconds (1 second)
            self.master.after(1000, update_traffic_light)

        # Start the loop by calling the update function
        update_traffic_light()


def main():
    root = tk.Tk()
    TrafficLightPage(root)
    root.mainloop()


if __name__ == "__main__":
    main()

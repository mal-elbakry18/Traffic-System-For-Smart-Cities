from PyQt5.QtGui import QCursor, QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QSlider, QLabel, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt, QTimer

class TrafficLightWidget(QWidget):
    def __init__(self, parent=None):
        super(TrafficLightWidget, self).__init__(parent)
        self.state = "RED"

    def paintEvent(self, event):
        painter = QPainter(self)
        if self.state == "RED":
            painter.setBrush(QColor(Qt.red))
        elif self.state == "YELLOW":
            painter.setBrush(QColor(Qt.yellow))
        elif self.state == "GREEN":
            painter.setBrush(QColor(Qt.green))
        painter.drawEllipse(0, 0, self.width(), self.height())

class TrafficLightGUI(QMainWindow):
    def __init__(self, intersection):
        super().__init__()
        self.intersection = intersection

        # Create a central widget to hold the layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create a vertical layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Add a label for the time and state
        self.label = QLabel()
        self.layout.addWidget(self.label)

        # Add a label and a slider for the number of cars for traffic light 1
        self.slider1_layout = QHBoxLayout()
        self.label1 = QLabel("Traffic Light 1 Cars")
        self.slider1_layout.addWidget(self.label1)
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setRange(0, 50)
        self.slider1.setFixedWidth(400)  # Set the width of the slider
        self.slider1_layout.addWidget(self.slider1)
        self.slider1_layout.addStretch(1)  # Add a stretch factor to push the slider towards the label
        self.layout.addLayout(self.slider1_layout)

        # Add a label and a slider for the number of cars for traffic light 2
        self.slider2_layout = QHBoxLayout()
        self.label2 = QLabel("Traffic Light 2 Cars")
        self.slider2_layout.addWidget(self.label2)
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setRange(0, 50)
        self.slider2.setFixedWidth(400)  # Set the width of the slider
        self.slider2_layout.addWidget(self.slider2)
        self.slider2_layout.addStretch(1)  # Add a stretch factor to push the slider towards the label
        self.layout.addLayout(self.slider2_layout)

        # Add a "Run" and "Stop" button in a horizontal layout
        self.button_layout = QHBoxLayout()
        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.run)
        self.run_button.setFixedWidth(100)  # Set the width of the button
        self.run_button.setFixedHeight(50)
        self.run_button.setStyleSheet("background-color: black; border-radius: 20px; color: white;")  # Style the button
        self.run_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_layout.addWidget(self.run_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop)
        self.stop_button.setFixedWidth(100)  # Set the width of the button
        self.stop_button.setFixedHeight(50)
        self.stop_button.setStyleSheet("background-color: black; border-radius: 20px; color: white;")  # Style the button
        self.stop_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_layout.addWidget(self.stop_button)
        self.layout.addLayout(self.button_layout)

        # Create a timer for the update method
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)

        # Variable to control the operation of the intersection
        self.running = False

    def run(self):
        self.running = True
        self.timer.start(1000)  # Call update every 1000 ms

    def stop(self):
        self.running = False
        self.timer.stop()

    def update(self):
        if self.running:
            # Use the slider values to add cars
            for _ in range(self.slider1.value()):
                self.intersection.light1.add_car()
            for _ in range(self.slider2.value()):
                self.intersection.light2.add_car()

            self.intersection.operate(1)
            text = (f"After {self.intersection.light1.time_in_state} seconds:\n"
                    f"{self.intersection.light1.name} is {self.intersection.light1.state} with {self.intersection.light1.car_count} cars waiting.\n"
                    f"{self.intersection.light2.name} is {self.intersection.light2.state} with {self.intersection.light2.car_count} cars waiting.")
            # Update the label with the new state
            self.label.setText(text)

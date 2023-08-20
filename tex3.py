
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QTextEdit
import cv2
from gaze_tracking import GazeTracking
import csv
import sys
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
import time

class GazeTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.add_step("STEP 1: Open the website to analyze", layout)
        self.website_input = self.add_input_field("Website URL", layout)
        self.add_button("Capture Screenshot", self.capture_screenshot, layout)

        self.add_step("STEP 2: Start Gaze Tracking", layout)
        self.add_button("Start Gaze Tracking", self.start_gaze_tracking, layout)

        self.add_step("STEP 3: Analyze Data", layout)
        self.add_button("Start Data Analysis", self.visualize_data, layout)

        central_widget.setLayout(layout)

        self.gaze = None

    def add_step(self, text, layout):
        step_label = QLabel(text)
        layout.addWidget(step_label)

    def add_input_field(self, placeholder, layout):
        input_field = QLineEdit(self)
        input_field.setPlaceholderText(placeholder)
        layout.addWidget(input_field)
        return input_field

    def add_button(self, text, callback, layout):
        button = QPushButton(text)
        button.clicked.connect(callback)
        layout.addWidget(button)

    def capture_screenshot(self):
        website_url = self.website_input.text().strip()
        if website_url:
            self.driver = webdriver.Chrome()
            self.driver.get(website_url)
            time.sleep(2)
            self.driver.get_screenshot_as_file("screenshot.png")

    def start_gaze_tracking(self):
        if self.gaze is None:
            self.gaze = GazeTracking()
            self.webcam = cv2.VideoCapture(0)
            self.csv_file = open('gaze_data.csv', 'w', newline='')
            self.csv_writer = csv.writer(self.csv_file)

        while True:
            ret, frame = self.webcam.read()

            self.gaze.refresh(frame)
            frame = self.gaze.annotated_frame()
            text = ""

            if self.gaze.is_blinking():
                text = "Blinking"
            elif self.gaze.is_right():
                text = "Looking right"
            elif self.gaze.is_left():
                text = "Looking left"
            elif self.gaze.is_center():
                text = "Looking center"

            cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

            left_pupil = self.gaze.pupil_left_coords()
            if left_pupil is not None:
                x, y = left_pupil
                self.csv_writer.writerow([x, y])

            cv2.imshow("Gaze Tracking", frame)

            if cv2.waitKey(1) == 27:
                break

        self.webcam.release()
        cv2.destroyAllWindows()
        self.csv_file.close()
        self.gaze = None

    def visualize_data(self):
        arr = np.loadtxt('gaze_data.csv', delimiter=',')
        plt.scatter(arr[:, 0], arr[:, 1], color='red', s=10)
        # Set the x and y axis limits
        img = plt.imread("screenshot.png")
        plt.imshow(img)

        x_min = arr[:, 0].min() - 30 # Adjust the value as needed
        x_max = arr[:, 0].max() + 30  # Adjust the value as needed
        y_min = arr[:, 1].min() - 30  # Adjust the value as needed
        y_max = arr[:, 1].max() + 30  # Adjust the value as needed
        plt.xlim(x_min, x_max)
        plt.ylim(y_min, y_max)

        plt.show()


def main():
    app = QApplication(sys.argv)
    window = GazeTrackerApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()

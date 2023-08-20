from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QTextEdit
from PySide6.QtGui import QFont
import cv2
from gaze_tracking import GazeTracking
import sys
import matplotlib.pyplot as plt
import numpy as np
from selenium import webdriver
import time
class GazeTrackerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gaze_data = []  # Initialize the gaze_data list
        self.init_ui()
    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        step_font = self.create_font(size=30)  # You can adjust the size here
        self.add_step("STEP 1: Open the website to analyze", layout, font=step_font)
        self.website_input = self.add_input_field("Website URL", layout)
        self.add_button("Capture Screenshot", self.capture_screenshot, layout, font=step_font)
        self.add_step("STEP 2: Start Gaze Tracking", layout, font=step_font)
        self.add_button("Start Gaze Tracking", self.start_gaze_tracking, layout, font=step_font)
        self.add_step("STEP 3: Analyze Data", layout, font=step_font)
        self.add_button("Start Data Analysis", self.visualize_data, layout, font=step_font)
        central_widget.setLayout(layout)
        self.gaze = None

    def add_step(self, text, layout, font=None):
        step_label = QLabel(text)
        if font:
            step_label.setFont(font)
        layout.addWidget(step_label)

    def create_font(self, size):
        font = QFont("Arial", size)
        return font
    def add_input_field(self, placeholder, layout, font=30):
        input_field = QLineEdit(self)
        input_field.setPlaceholderText(placeholder)
        layout.addWidget(input_field)
        return input_field

    def add_button(self, text, callback, layout, font=30):
        button = QPushButton(text)
        button.clicked.connect(callback)
        layout.addWidget(button)

    def capture_screenshot(self):
        website_url = self.website_input.text().strip()
        if website_url:
            self.driver = webdriver.Chrome()
            self.driver.get(website_url)
            time.sleep(5)
            self.driver.get_screenshot_as_file("screenshot.png")

    def start_gaze_tracking(self):
        if self.gaze is None:
            self.gaze = GazeTracking()
            self.webcam = cv2.VideoCapture(0)

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
                self.gaze_data.append([left_pupil[0], left_pupil[1]])
            cv2.imshow("Gaze Tracking", frame)
            if cv2.waitKey(1) == 27:
                break

        self.webcam.release()
        cv2.destroyAllWindows()
        self.gaze = None

    def visualize_data(self):
        if not self.gaze_data:
            return
        arr = np.array(self.gaze_data)
        x_min = max(arr[:, 0].min() - 10, 0)
        x_max = min(arr[:, 0].max() + 10, 500)
        y_min = max(arr[:, 1].min() - 10, 0)
        y_max = min(arr[:, 1].max() + 10, 300)
        fig, ax = plt.subplots()
        ax.scatter(arr[:, 0], arr[:, 1], color='red', s=10)
        img = plt.imread("screenshot.png")
        ax.imshow(img, extent=[x_min, x_max, y_max, y_min], aspect='auto', origin='lower')
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        plt.show()

def main():
    app = QApplication(sys.argv)
    window = GazeTrackerApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
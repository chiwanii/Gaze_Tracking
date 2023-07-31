# File: main.py
import sys
import os
import argparse
import time
import cv2
import io
from gaze_tracking import GazeTracking
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QIODevice, Qt, QSize, Slot, QThread
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QLineEdit, QLabel, QPushButton, QTableWidgetItem
from PySide6.QtGui import QAction, QImage, QPixmap

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "Gui_test1.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    sys.exit(app.exec())

## how to implement this programm in the gui programm
class Gazetracking():
    def __init__(self, parent=None, medialoader=None, statusbar=None, detector=None, img_viewer=None):
        super().__init__(parent=parent)
        self.medialoader = medialoader if medialoader is not None else self.parent().medialoader
        self.sbar = statusbar if statusbar is not None else self.parent().sbar
        self.detector = detector
        self.viewer = img_viewer

        self.stop = False
        def run(self):
         gaze = GazeTracking()
         webcam = cv2.VideoCapture(0)

        while True:
            # We get a new frame from the webcam
            _, frame = webcam.read()

            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)

            frame = gaze.annotated_frame()
            text = ""

            if gaze.is_blinking():
                text = "Blinking"
            elif gaze.is_right():
                text = "Looking right"
            elif gaze.is_left():
                text = "Looking left"
            elif gaze.is_center():
                text = "Looking center"

            cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()
            cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
            cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

            cv2.imshow("Demo", frame)

            if cv2.waitKey(1) == 27:
                break

        webcam.release()
        cv2.destroyAllWindows()

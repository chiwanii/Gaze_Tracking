from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QTextEdit
import cv2
from gaze_tracking import GazeTracking
import csv
import sys
import webbrowser
import time
import datetime
import threading


#-- encoding: utf-8 -- 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget1 = QLabel("STEP 1: Please open the website you would like to analyse")
        font = widget1.font()
        font.setPointSize(15)
        widget1.setFont(font)
        
        ## it needs more input function
        widget2 = QLineEdit(self)
        font = widget2.font()
        font.setPointSize(15)
        widget2.setFont(font)

        widget5 = QPushButton("Go to the web adress")
        font = widget5.font()
        font.setPointSize(5)
        widget5.setFont(font)
        widget5.clicked.connect(self.open_website)

        widget3 = QLabel("STEP 2: please set your head to camera and start the gaze tracking.")
        font = widget3.font()
        font.setPointSize(15)
        widget3.setFont(font)

        widget4 = QPushButton("Gaze Tracking start")
        font = widget4.font()
        font.setPointSize(15)
        widget4.setFont(font)
        widget4.clicked.connect(self.gaze_tracking)
        
        widget6 = QLabel("Press ESC if you want to quit") ## create it as a Quit button 
        font = widget6.font()
        font.setPointSize(15)
        widget6.setFont(font)


        ## step3: read the data and analyze the data

        widget7 = QLabel("STEP 3: press the button, to start the data processing")
        font = widget7.font()
        font.setPointSize(15)
        widget7.setFont(font)

        widget8 = QPushButton("Data analyzing start")
        font = widget8.font()
        font.setPointSize(15)
        widget8.setFont(font)
        #widget8.clicked.connect(self.gaze_tracking)

        layout = QVBoxLayout()
        layout.addWidget(widget1)
        layout.addWidget(widget2)
        layout.addWidget(widget5)
        layout.addWidget(widget3)
        layout.addWidget(widget4)
        layout.addWidget(widget6)
        layout.addWidget(widget7)
        layout.addWidget(widget8)


        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def open_website(self):
        website_url = self.sender().parent().findChild(QLineEdit).text()
        if website_url.strip() != "":
            webbrowser.open(website_url)

    def button_event(self):
        text = self.widget2.toPlainText() # load the text_edit text
        self.text_label.setText(text) # set up the text

        ## https://github.com/antoinelame/GazeTracking
    def gaze_tracking(self):
        gaze = GazeTracking()
        webcam = cv2.VideoCapture(0)
        with open('C:/Users/skqkr/source/repos/GazeTracking/t1.csv', 'w', newline='') as f:
            writer = csv.writer(f)

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

                def print_check():    
                 if left_pupil != None:
                     print("Current Eye position:", str(left_pupil))
    
                def save_check():
                    if left_pupil != None:
                            x, y = left_pupil
                            writer.writerow([x, y])

                print_check()
                save_check()
                cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
                cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

                cv2.imshow("Demo", frame)

                if cv2.waitKey(1) == 27:
                    break
   
            webcam.release()
            cv2.destroyAllWindows()
            f.close()

app = QApplication(sys.argv)
window = MainWindow()
window.show()


app.exec()

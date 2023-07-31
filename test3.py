#!/usr/bin/python

import sys

from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QVBoxLayout, QWidget


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        hbox = QVBoxLayout(self)
        
        self.lbl = QLabel(self)
        qle = QLineEdit(self)

        qle.textChanged[str].connect(self.onChanged)

        hbox.addWidget(self.lbl)
        hbox.addSpacing(20)
        hbox.addWidget(qle)

        self.setGeometry(400, 400, 350, 300)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, text):

        self.lbl.setText(text)
        self.lbl.adjustSize()


def main():
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
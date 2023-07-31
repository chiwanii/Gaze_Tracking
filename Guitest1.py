# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gui_test1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_testBtn(object):
    def setupUi(self, testBtn):
        if not testBtn.objectName():
            testBtn.setObjectName(u"testBtn")
        testBtn.resize(800, 600)
        self.centralwidget = QWidget(testBtn)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(450, 60, 75, 24))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 30, 391, 16))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 60, 381, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 190, 391, 16))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(440, 180, 75, 24))
        testBtn.setCentralWidget(self.centralwidget)
        #self.menubar = QMenuBar(testBtn)
        #self.menubar.setObjectName(u"menubar")
        #self.menubar.setGeometry(QRect(0, 0, 800, 22))
        #testBtn.setMenuBar(self.menubar)
        #self.statusbar = QStatusBar(testBtn)
        #self.statusbar.setObjectName(u"statusbar")
        #testBtn.setStatusBar(self.statusbar)

        self.retranslateUi(testBtn)
        self.pushButton.clicked.connect(testBtn.Web_go)

        QMetaObject.connectSlotsByName(testBtn)
    # setupUi

    def retranslateUi(self, testBtn):
        testBtn.setWindowTitle(QCoreApplication.translate("testBtn", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("testBtn", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("testBtn", u"STEP 1: \ubd84\uc11d\ud560 \uc6f9\uc0ac\uc774\ud2b8\ub97c \uc5f4\uc5b4 \uc8fc\uc138\uc694.", None))
        self.lineEdit.setText(QCoreApplication.translate("testBtn", u"\ubd84\uc11d\ud560 \uc6f9 \uc0ac\uc774\ud2b8 \uc8fc\uc18c", None))
        self.label_2.setText(QCoreApplication.translate("testBtn", u"STEP 2: \uce74\uba54\ub77c\uc5d0 \ub0b4 \uc5bc\uad74\uc744 \ub9de\ucd98 \ud6c4, \ub208\ub3d9\uc790 \uce21\uc815 \uc124\uc815\uc744 \uc2dc\uc791\ud574 \uc8fc\uc138\uc694.", None))
        self.pushButton_2.setText(QCoreApplication.translate("testBtn", u"\uce21\uc815 \uc2dc\uc791", None))
    # retranslateUi


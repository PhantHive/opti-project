from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLabel, QStackedWidget, QHBoxLayout, QVBoxLayout, \
    QWidget, QListWidget, QStackedLayout
import sys

class IPWindow(object):
    def setupUI(self, IPWindow):
        IPWindow.setGeometry(500, 100, 1000, 500)
        IPWindow.setFixedSize(1000, 500)
        IPWindow.setWindowTitle("Pjmat - The Real Flow \ Ip")
        font = QFont('aero')
        QFontDatabase.addApplicationFont('assets/font/aero.ttf')
        self.IpWidgets = QWidget(IPWindow)

        self.labelIp = QLabel(self.IpWidgets)
        self.labelIp.setText("Pjmat\ \nIp_CALCULATOR")
        self.labelIp.setFont(font)
        self.labelIp.move(50, 50)
        self.labelIp.resize(700, 70)
        self.labelIp.setStyleSheet("font-size: 40px")

        # Button Ip page
        self.homeBt = QPushButton(self.IpWidgets)
        self.homeBt.setText("HOME")
        self.homeBt.setFont(font)
        self.homeBt.move(800, 420)
        self.homeBt.resize(120, 55)

        # Button flight plan page
        self.fpBt = QPushButton(self.IpWidgets)
        self.fpBt.setText("FLIGHT PLAN")
        self.fpBt.setFont(font)
        self.fpBt.move(600, 420)
        self.fpBt.resize(170, 55)

        self.gui()

        IPWindow.setCentralWidget(self.IpWidgets)

    def gui(self):
        # PLANE CHOICE
        self.selectPlane = QLabel(self.IpWidgets)
        self.selectPlane.setText("select plane")
        self.selectPlane.setFont(font)
        self.selectPlane.move(125, 300)
        self.selectPlane.resize(400, 250)
        self.selectPlane.setObjectName("planeSel")

        self.labelImage = QLabel(self.IpWidgets)
        self.labelImage.move(50, 150)
        self.labelImage.resize(400, 250)
        self.labelImage.setObjectName("planeLabel")
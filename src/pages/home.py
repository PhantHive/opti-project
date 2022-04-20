from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLabel, QStackedWidget, QHBoxLayout, QVBoxLayout, \
    QWidget, QListWidget, QStackedLayout
import sys

class Main(object):
    def setupUI(self, Main):
        Main.setGeometry(500, 100, 1000, 500)
        Main.setFixedSize(1000, 500)
        Main.setWindowTitle("MATH PROJECT - IPSA 2021")
        font = QFont('aero')
        QFontDatabase.addApplicationFont('src/font/NeoEuler.ttf')
        self.mainWidget = QWidget(Main)

        self.label = QLabel(self.mainWidget)
        self.label.setText("MATH PROJECT")
        self.label.setFont(font)
        self.label.move(50, 50)
        self.label.resize(400, 70)

        # Button Iter Power Page
        self.ipBt = QPushButton(self.mainWidget)
        self.ipBt.setText("Iter Power")
        self.ipBt.setFont(font)
        self.ipBt.move(800, 420)
        self.ipBt.resize(120, 55)

        Main.setCentralWidget(self.mainWidget)
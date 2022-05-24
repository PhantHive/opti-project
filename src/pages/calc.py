from decimal import Decimal

import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QLineEdit, QComboBox
from src.canvas.Canvas import Canvas


class Calculator(object):

    def __init__(self):
        '''
        every possible configuration
        '''
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = int(self.screen.width() * 0.50)
        self.height = int(self.screen.height() * 0.55)

        self.lang = None
        self.home_bt = None

        self.onlyInt = QIntValidator()

    def setupUI(self, Calculator):
        Calculator.setGeometry(500, 100, 1200, 780)
        Calculator.setFixedSize(1200, 780)
        Calculator.setWindowTitle("MATH PROJECT - IPSA 2021 \ Puissance Itérée Inverse")

        self.CWidgets = QWidget(Calculator)

        self.entry_widgets()
        self.result_widgets()
        self.move_widgets()

        Calculator.setCentralWidget(self.CWidgets)


    def entry_widgets(self):

        self.language = QPushButton(self.CWidgets)
        self.language.setText(self.lang["language"])

        self.home_bt = QPushButton(self.CWidgets)
        self.home_bt.setText(self.lang["home"])

        self.home_bt.resize(130, 55)
        self.home_bt.setProperty("type", 1)

    def result_widgets(self):

        pass

    def move_widgets(self):

        self.language.move(int(self.width * 0.95), int(self.height * 0.015))

        self.home_bt.move(int(self.width * 0.85), int(self.height * 0.9))

    def calculate(self):

        pass

from decimal import Decimal

import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import (
    QPushButton,
    QLabel,
    QWidget,
    QLineEdit,
    QComboBox,
    QGraphicsDropShadowEffect,
)

from src.canvas.Canvas import Canvas


class StartWin(object):
    def __init__(self):
        """
        choose the equation to solve within a specific interval
        """

        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = int(self.screen.width() * 0.50)
        self.height = int(self.screen.height() * 0.55)

        self.onlyInt = QIntValidator()
        self.lang = None

        self.change_eq = None  # change equation
        self.home_bt = None
        self.intervalx = None
        self.intervaly = None
        self.equation = None

    def setupUI(self, StartWin):
        StartWin.setGeometry(
            (self.screen.width() - self.width) // 2,
            (self.screen.height() - self.height) // 2,
            self.width,
            self.height,
        )
        StartWin.setFixedSize(self.width, self.height)

        StartWin.setWindowTitle(self.lang["app-title"] + " \ " + self.lang["start"])

        self.start_widgets = QWidget(StartWin)

        self.language = QPushButton(self.start_widgets)
        self.language.setText(self.lang["language"])

        self.entry_widgets()
        self.result_widgets()
        self.move_widgets()

        StartWin.setCentralWidget(self.start_widgets)

    def entry_widgets(self):
        # self.calcul.clicked.connect(self.calculate)
        self.home_bt = QPushButton(self.start_widgets)
        self.home_bt.setText(self.lang["home"])

        self.home_bt.resize(130, 55)
        self.home_bt.setProperty("type", 1)

        self.intervalx = QLineEdit(self.start_widgets)
        self.intervalx.setPlaceholderText(self.lang["intervalx-entry"])
        self.intervalx.resize(250, 45)

        self.intervaly = QLineEdit(self.start_widgets)
        self.intervaly.setPlaceholderText(self.lang["intervaly-entry"])
        self.intervaly.resize(250, 45)

        self.equation = QLabel(self.start_widgets)
        self.equation.resize(250, 45)
        self.equation.setText("Equation: ")
        self.equation.setProperty("type", 2)

        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(Qt.black)
        shadow.setBlurRadius(25)
        shadow.setOffset(1, 1)

        self.change_eq = QPushButton(self.start_widgets)  # change equation
        self.change_eq.resize(250, 45)
        self.change_eq.setText(self.lang["change-equation"])
        self.change_eq.setProperty("type", 2)

        self.method = QPushButton(self.start_widgets)  # change equation
        self.method.resize(250, 45)
        self.method.setText(self.lang["change-method"])
        self.method.setProperty("type", 2)

        self.intervalx.setGraphicsEffect(shadow)
        self.intervaly.setGraphicsEffect(shadow)
        self.change_eq.setGraphicsEffect(shadow)
        self.method.setGraphicsEffect(shadow)

    def start_change_equ(self):
        pass

    def result_widgets(self):
        # Result
        pass

    def move_widgets(self):

        self.language.move(int(self.width * 0.95), int(self.height * 0.015))
        self.change_eq.move(int(self.width * 0.1), int(self.height * 0.15))

        self.intervalx.move(int(self.width * 0.1), int(self.height * 0.5))
        self.intervaly.move(int(self.width * 0.1), int(self.height * 0.6))
        self.equation.move(int(self.width * 0.1), int(self.height * 0.30))

        self.method.move(int(self.width * 0.5), int(self.height * 0.75))
        self.home_bt.move(int(self.width * 0.85), int(self.height * 0.9))

    def calculate(self):
        pass

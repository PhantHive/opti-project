from decimal import Decimal

import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

from src.canvas.Canvas import Canvas


class EquationWin(object):

    def __init__(self):
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = int(self.screen.width() * 0.50)
        self.height = int(self.screen.height() * 0.55)

        self.onlyInt = QIntValidator()
        self.lang = None

    def setupUI(self, EquationWin):
        EquationWin.setGeometry(
            (self.screen.width() - self.width) // 2,
            (self.screen.height() - self.height) // 2,
            self.width,
            self.height,
        )
        EquationWin.setFixedSize(self.width, self.height)

        EquationWin.setWindowTitle(self.lang["app-title"] + " \ " +
                                   self.lang["unk"])

        self.start_widgets = QWidget(EquationWin)

        self.language = QPushButton(self.start_widgets)
        self.language.setText(self.lang["language"])

        self.entry_widgets()
        self.result_widgets()
        self.move_widgets()

        EquationWin.setCentralWidget(self.start_widgets)

    def entry_widgets(self):
        self.home_bt = QPushButton(self.start_widgets)
        self.home_bt.setText(self.lang["home"])

        self.home_bt.resize(130, 55)
        self.home_bt.setProperty("type", 1)

        self.equa1 = QPushButton(self.change_equation)  # change to equation 1
        self.equa1.resize(250, 45)
        self.equa1.setText(self.lang["unk"])
        self.equa1.setProperty("type", 2)

        self.equa2 = QPushButton(self.change_equation)  # change to equation 2
        self.equa2.resize(250, 45)
        self.equa2.setText(self.lang["unk"])
        self.equa2.setProperty("type", 2)

        self.equa3 = QPushButton(self.change_equation)  # change to equation 3
        self.equa3.resize(250, 45)
        self.equa3.setText(self.lang["unk"])
        self.equa3.setProperty("type", 2)

        self.equa4 = QPushButton(self.change_equation)  # change to equation 4
        self.equa4.resize(250, 45)
        self.equa4.setText(self.lang["unk"])
        self.equa4.setProperty("type", 2)

        self.equa5 = QPushButton(self.change_equation)  # change to equation 5
        self.equa5.resize(250, 45)
        self.equa5.setText(self.lang["unk"])
        self.equa5.setProperty("type", 2)

    def return_start(self):
        pass

    def change_equation(self, a):
        print(a)

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
        StartWin.setGeometry((self.screen.width() - self.width) // 2, (self.screen.height() - self.height) // 2,
                             self.width, self.height)
        StartWin.setFixedSize(self.width, self.height)

        StartWin.setWindowTitle(self.lang["app-title"] + " \ " + self.lang["start"])

        self.change_equation = QWidget(StartWin)


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

    def result_widgets(self):
        # Result
        pass

    def move_widgets(self):

        self.language.move(int(self.width * 0.95), int(self.height * 0.015))
        self.change_eq.move(int(self.width * 0.1), int(self.height * 0.15))
        self.intervalx.move(int(self.width * 0.5), int(self.height * 0.35))
        self.intervaly.move(int(self.width * 0.5), int(self.height * 0.45))
        self.equation.move(int(self.width * 0.1), int(self.height * 0.55))
        self.method.move(int(self.width * 0.5), int(self.height * 0.75))
        self.home_bt.move(int(self.width * 0.85), int(self.height * 0.9))

"""

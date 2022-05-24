import json
from decimal import Decimal

import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtSvg
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

from src.canvas.Canvas import Canvas
from src.datas.text2svg import Tex2Svg
from src.maths.functions import Functions
from src.pages.calculator import EquationWin


class StartWin(object):
    def __init__(self):
        """
        choose the equation to solve within a specific interval
        """

        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = int(self.screen.width() * 0.50)
        self.height = int(self.screen.height() * 0.55)
        self.formula = json.load(open("src/datas/equations.json"))

        self.onlyInt = QIntValidator()
        self.lang = None

        self.change_eq = None  # change equation
        self.home_bt = None
        self.intervalx = None
        self.intervaly = None
        self.equation = None

        self.fct = Functions()

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

        self.ui_ch_eq = EquationWin()

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

        svgText = Tex2Svg(self.formula["1"])
        self.viewer = QtSvg.QSvgWidget(self.start_widgets)
        self.viewer.load(svgText.tex2svg())
        self.viewer.setProperty("type", 2)
        self.viewer.resize(400, 350)

        """self.equation = QLabel(self.start_widgets)
        self.equation.resize(250, 55)
        self.equation.setProperty("type", 2)"""

        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(Qt.black)
        shadow.setBlurRadius(25)
        shadow.setOffset(1, 1)

        self.change_eq = QPushButton(self.start_widgets)  # change equation
        self.change_eq.resize(250, 45)
        self.change_eq.setText(self.lang["change-equation"])
        self.change_eq.setProperty("type", 2)

        self.method = QPushButton(self.start_widgets)  # change method
        self.method.resize(250, 45)
        self.method.setText(self.lang["change-method"])
        self.method.setProperty("type", 2)

        self.change_eq.clicked.connect(self.start_change_equ)

        self.intervalx.setGraphicsEffect(shadow)
        self.intervaly.setGraphicsEffect(shadow)
        self.change_eq.setGraphicsEffect(shadow)
        self.method.setGraphicsEffect(shadow)

        self.change_eq.clicked.connect(self.start_change_equ)
        # self.calculator = EquationWin(self.lang)

    def start_change_equ(self):
        """
        self.ui_ch_eq.lang = self.lang
        self.ui_ch_eq.setupUI(self)
        self.ui_ch_eq.home_bt.clicked.connect(self.startMainWindow)
        self.ui_ch_eq.language.clicked.connect(self.change_language)
        self.page = "change equation"
        self.show()

                self.ui_start.home_bt.clicked.connect(self.startMainWindow)
                self.ui_start.language.clicked.connect(self.change_language)
                self.page = "start"
                self.show()
        """

        i = self.fct.get_equation()
        if i == 2:
            self.fct.set_equation(1)
        else:
            self.fct.set_equation(i + 1)

        svgText = Tex2Svg(self.formula[str(i)])
        self.viewer.load(svgText.tex2svg())

    def start_method(self):

        # self.calculator.show()
        # self.calculator.setupUI()
        pass

    def result_widgets(self):
        # Result
        pass

    def move_widgets(self):

        self.language.move(int(self.width * 0.95), int(self.height * 0.015))

        self.change_eq.move(int(self.width * 0.6), int(self.height * 0.25))
        # self.equation.move(int(self.width * 0.1), int(self.height * 0.3))

        self.viewer.move(int(self.width * 0.1), int(self.height * 0.2))

        self.intervalx.move(int(self.width * 0.7), int(self.height * 0.4))
        self.intervaly.move(int(self.width * 0.7), int(self.height * 0.55))

        self.method.move(int(self.width * 0.6), int(self.height * 0.7))

        self.home_bt.move(int(self.width * 0.85), int(self.height * 0.9))

    def calculate(self):
        pass

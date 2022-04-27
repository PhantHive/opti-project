from decimal import Decimal

import numpy as np
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QLineEdit, QComboBox
from src.canvas.Canvas import Canvas


class IVWindow(object):

    def __init__(self):
        '''
        every possible configuration
        '''

        self.onlyInt = QIntValidator()

    def setupUI(self, IVWindow):
        IVWindow.setGeometry(500, 100, 1200, 780)
        IVWindow.setFixedSize(1200, 780)
        IVWindow.setWindowTitle("MATH PROJECT - IPSA 2021 \ Puissance Itérée Inverse")

        self.IVWidgets = QWidget(IVWindow)

        self.entry_widgets()
        self.result_widgets()
        self.move_widgets()

        IVWindow.setCentralWidget(self.IVWidgets)


    def entry_widgets(self):

        pass

    def result_widgets(self):

        pass

    def move_widgets(self):

        pass

    def calculate(self):

        pass

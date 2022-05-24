from decimal import Decimal

import numpy as np
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QLineEdit, QComboBox
from src.canvas.Canvas import Canvas


class Config(object):

    def __init__(self):
        '''
        every possible configuration
        '''

        self.lang = None

    def setupUI(self, Config):
        Config.setGeometry(500, 100, 150, 250)
        Config.setFixedSize(150, 250)
        Config.setWindowTitle(self.lang["app-title"] + " \ " + self.lang["start"] + " \ " + self.lang["calc"])

        self.IVWidgets = QWidget(Config)

        self.entry_widgets()
        self.result_widgets()
        self.move_widgets()

        Config.setCentralWidget(self.IVWidgets)


    def entry_widgets(self):

        pass

    def result_widgets(self):

        pass

    def move_widgets(self):

        pass

    def calculate(self):

        pass

from decimal import Decimal

import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QRadioButton, \
    QGraphicsDropShadowEffect
from src.canvas.Canvas import Canvas
from src.maths.functions import Functions
from src.maths.graph import Graph


class Calculator(object):

    def __init__(self):
        '''
        every possible configuration
        '''
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = int(self.screen.width() * 0.70)
        self.height = int(self.screen.height() * 0.50)

        self.lang = None
        self.back_bt = None

        self.onlyInt = QIntValidator()

    def setupUI(self, Calculator):
        Calculator.setGeometry(500, 100, 1200, 600)
        Calculator.setFixedSize(1200, 600)
        Calculator.setWindowTitle(self.lang["app-title"] + " \ " + self.lang["start"] + " \ " + self.lang["calc"])

        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(Qt.black)
        shadow.setBlurRadius(25)
        shadow.setOffset(1, 1)

        self.CWidgets = QWidget(Calculator)
        self.ChoiceWidgets = QWidget(self.CWidgets)

        self.layout = QVBoxLayout(self.ChoiceWidgets)
        self.method_1 = QRadioButton("Gradient 1")
        self.method_1.setChecked(True)

        self.method_2 = QRadioButton("Gradient 3")

        self.method_3 = QRadioButton("Gradient 3")

        self.layout.addWidget(self.method_1)
        self.layout.addWidget(self.method_2)
        self.layout.addWidget(self.method_3)

        self.method_1.toggled.connect(lambda: self.btn_state(self.method_1))
        self.method_2.toggled.connect(lambda: self.btn_state(self.method_2))
        self.method_3.toggled.connect(lambda: self.btn_state(self.method_3))

        self.method_1.setGraphicsEffect(shadow)
        self.method_2.setGraphicsEffect(shadow)
        self.method_3.setGraphicsEffect(shadow)

        self.layout.setSpacing(50)

        Calculator.setLayout(self.layout)

        # ligne
        '''painter = QPainter(Calculator)
        pen = QPen(Qt.white, 5)
        pixmap = QPixmap("./src/image/bg.jpg")
        painter.drawPixmap(Calculator, pixmap)
        painter.setPen(pen)
        painter.drawLine(100, 100, 100, 200)'''

        self.entry_widgets()
        self.result_widgets()
        self.move_widgets()

        Calculator.setCentralWidget(self.CWidgets)

    def btn_state(self, btn):

        if btn.text() == "method_1":
            if btn.isChecked() == True:
                self.method_2.isChecked(False)
                self.method_3.isChecked(False)

        if btn.text() == "method_2":
            if btn.isChecked() == True:
                self.method_1.isChecked(False)
                self.method_3.isChecked(False)

        if btn.text() == "method_3":
            if btn.isChecked() == True:
                self.method_1.isChecked(False)
                self.method_2.isChecked(False)

    def entry_widgets(self):

        self.language = QPushButton(self.CWidgets)
        self.language.setText(self.lang["language"])

        self.back_bt = QPushButton(self.CWidgets)
        self.back_bt.setText(self.lang["back"])
        self.back_bt.resize(130, 55)
        self.back_bt.setProperty("type", 1)


        # function graph representation
        fct = Functions(None, None)
        # graphical part

        self.canvas = Canvas(self.CWidgets)
        self.canvas.resize(450, 275)
        self.canvas.surface(-3, 3, 0.1, fct, "g")

        self.fct_comment = QLabel(self.CWidgets)
        self.fct_comment.setText("Lorem ipsum dolor sit amet. Et ducimus omnis nam dolores \n"
                                 "quaerat quo perferendis soluta. \n"
                                 "Ad vero culpa vel placeat unde hic quia veniam et nihil ipsa. \n"
                                 "Et harum harum aut voluptatibus dolorum et laborum aperiam \n"
                                 "non velit repellendus.")
        self.fct_comment.resize(450, 150)
        self.fct_comment.setProperty("type", 2)



    def result_widgets(self):

        pass

    def move_widgets(self):

        self.language.move(int(self.width * 0.85), int(self.height * 0.01))

        self.back_bt.move(int(self.width * 0.78), int(self.height * 0.97))

        self.canvas.move(int(self.width * 0.45), int(self.height * 0.15))

        self.fct_comment.move(int(self.width * 0.45), int(self.height * 0.7))

        self.ChoiceWidgets.move(int(self.width * 0.15), int(self.height * 0.4))

    def calculate(self):

        pass

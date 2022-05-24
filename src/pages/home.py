from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLabel, QStackedWidget, QHBoxLayout, QVBoxLayout, \
    QWidget, QListWidget, QStackedLayout, QGraphicsDropShadowEffect
import sys

from src.lang.language import Language

class Main(object):

    def __init__(self):
        '''
        home menu: here you can select which page to start
        '''

        self.lang = None

    def setupUI(self, Main):

        screen = QtWidgets.QDesktopWidget().screenGeometry()
        width = int(screen.width() * 0.25)
        height = int(screen.height() * 0.55)
        Main.setGeometry((screen.width() - width) // 2, (screen.height() - height) // 2, width, height)
        Main.setFixedSize(width, height)
        Main.setWindowTitle(self.lang["app-title"])

        self.mainWidget = QWidget(Main)


        self.language = QPushButton(self.mainWidget)
        self.language.setText(self.lang["language"])
        self.language.move(int(width * 0.92), int(height * 0.015))


        self.title = QLabel(self.mainWidget)
        self.title.setText(self.lang["title"])
        self.title.resize(int(width * 0.65), 70)
        self.title.move((width - self.title.width()) // 2, int(height * 0.05))

        # Start Page
        self.start_bt = QPushButton(self.mainWidget)
        self.start_bt.setText(self.lang["start"])
        self.start_bt.resize(125, 55)
        self.start_bt.move((width - self.start_bt.width()) // 2, int(height * 0.3))

        '''# Config Page
        self.conf_bt = QPushButton(self.mainWidget)
        self.conf_bt.setText(self.lang["config"])
        self.conf_bt.resize(125, 55)
        self.conf_bt.move((width - self.conf_bt.width()) // 2, int(height * 0.5))'''

        # Credit Page
        self.credit_bt = QPushButton(self.mainWidget)
        self.credit_bt.setText(self.lang["credit"])
        self.credit_bt.resize(125, 55)
        self.credit_bt.move((width - self.start_bt.width()) // 2, int(height * 0.7))

        self.start_bt.setProperty("type", 1)
        #self.conf_bt.setProperty("type", 1)
        self.credit_bt.setProperty("type", 1)
        self.language.setProperty("type", 3)

        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(Qt.black)
        shadow.setBlurRadius(25)
        shadow.setOffset(1, 1)
        self.title.setGraphicsEffect(shadow)

        Main.setCentralWidget(self.mainWidget)


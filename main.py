from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow

import sys

from src.pages.calc import Calculator
from src.pages.config import IVWindow
from src.pages.start import StartWin
from src.pages.home import Main
from src.lang.language import Language
from src.pages.spe_fct import SpeFct


class GUI(QMainWindow):

    def __init__(self, parent=None):

        super(GUI, self).__init__(parent)
        self.language = Language("fr")
        self.page = None
        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('src/image/maths.png'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(self.icon)

        QtGui.QFontDatabase.addApplicationFont('./src/font/simplicity.ttf')

        self.uiMainWindow = Main()
        self.ui_start = StartWin()
        self.ui_calculator = Calculator()
        self.ui_spefct = SpeFct()
        self.ui_conf = IVWindow()
        self.startMainWindow()

    def startMainWindow(self):
        '''
        :return: the selection menu window
        '''
        self.uiMainWindow.lang = self.language.get_lang()
        self.uiMainWindow.setupUI(self)
        # Connect buttons to the page (ivPage, ipPage ...)
        self.uiMainWindow.start_bt.clicked.connect(self.load_start)
        self.uiMainWindow.conf_bt.clicked.connect(self.load_config)
        self.uiMainWindow.language.clicked.connect(self.change_language)
        self.page = "main"
        self.show()

    def load_start(self):
        '''
        :return: the equation selector menu
        '''

        self.ui_start.lang = self.language.get_lang()
        self.ui_start.setupUI(self)
        self.ui_start.home_bt.clicked.connect(self.startMainWindow)
        self.ui_start.language.clicked.connect(self.change_language)
        self.ui_start.method.clicked.connect(self.load_calc)
        self.ui_start.spe_fct.clicked.connect(self.load_spe_fct)
        self.page = "start"
        self.show()

    def load_calc(self):
        '''
        :return: the equation selector menu
        '''

        if self.ui_start.verif == True:
            self.ui_calculator.lang = self.language.get_lang()
            self.ui_calculator.setupUI(self)
            self.ui_calculator.back_bt.clicked.connect(self.load_start)
            self.ui_calculator.language.clicked.connect(self.change_language)

            self.page = "calc"
            self.show()

    def load_spe_fct(self):

        self.ui_spefct.lang = self.language.get_lang()
        self.ui_spefct.setupUI(self)
        self.ui_spefct.back_bt.clicked.connect(self.load_start)
        self.ui_spefct.language.clicked.connect(self.change_language)

        self.page = "Special Function"
        self.show()

    def load_config(self):
        '''
        :return: the configuration menu
        '''

        self.ui_conf.setupUI(self)
        # self.ui_conf.homeBt.clicked.connect(self.startMainWindow)
        self.page = "config"
        self.show()

    def change_language(self):
        '''
        :return: the corresponding dictionary of the selected language.
        '''

        if self.page == "main":
            if self.uiMainWindow.lang["language"] == "fr":
                self.language = Language("en")
            else:
                self.language = Language("fr")
            self.startMainWindow()
        elif self.page == "calc":
            if self.ui_calculator.lang["language"] == "fr":
                self.language = Language("en")
            else:
                self.language = Language("fr")
            self.load_calc()
        else:
            if self.ui_start.lang["language"] == "fr":
                self.language = Language("en")
            else:
                self.language = Language("fr")
            self.load_start()


if __name__ == '__main__':
    font = QFont('aero')
    app = QApplication(sys.argv)
    app.setStyle('Window')
    app.setStyleSheet(open('src/css/main.qss').read())
    window = GUI()
    sys.exit(app.exec_())

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QPushButton, QLabel, QWidget, QVBoxLayout, QRadioButton, \
    QGraphicsDropShadowEffect



class Credit(object):

    intervalx = [None, None]
    intervaly = [None, None]
    equation = 1

    def __init__(self):
        '''
        every possible configuration
        '''
        self.screen = QtWidgets.QDesktopWidget().screenGeometry()
        self.width = int(self.screen.width() * 0.70)
        self.height = int(self.screen.height() * 0.50)

        self.lang = None
        self.back_bt = None


    def setupUI(self, Credit):
        Credit.setGeometry(500, 100, 350, 550)
        Credit.setFixedSize(400, 700)
        Credit.setWindowTitle(self.lang["app-title"] + " \ " + "Credit")

        shadow = QGraphicsDropShadowEffect()
        shadow.setColor(Qt.black)
        shadow.setBlurRadius(25)
        shadow.setOffset(1, 1)


        self.CWidgets = QWidget(Credit)


        self.entry_widgets()
        self.result_widgets()
        self.move_widgets()

        Credit.setCentralWidget(self.CWidgets)



    def entry_widgets(self):

        self.language = QPushButton(self.CWidgets)
        self.language.setText(self.lang["language"])

        self.back_bt = QPushButton(self.CWidgets)
        self.back_bt.setText(self.lang["back"])
        self.back_bt.resize(130, 55)
        self.back_bt.setProperty("type", 1)

        self.credit = QLabel(self.CWidgets)
        self.credit.setText(f"\t☾ CREDIT ☽"
                            f"\n\n\n✪School: IPSA (Paris) "
                            f"\n\n✪Teacher: "
                            f"\n\tBletzecker"
                            f"\n\tPeschard "
                            f"\n\n✪Students: "
                            f"\n\tCorentin "
                            f"\n\tEvan "
                            f"\n\tWenceslas"
                            f"\n\tZakaria")
        self.credit.resize(270, 550)
        self.credit.setProperty("type", 1)


    def result_widgets(self):

        pass

    def move_widgets(self):

        self.language.move(int(self.width * 0.85), int(self.height * 0.01))
        self.back_bt.move(int(self.width * 0.1), int(self.height * 1.17))
        self.credit.move(int(self.width * 0.02), int(self.height * 0.15))

    def calculate(self):

        pass

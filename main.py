from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QPushButton, QApplication, QMainWindow, QLabel, QStackedWidget, QHBoxLayout, QVBoxLayout, \
    QWidget, QListWidget, QStackedLayout
import sys


from src.pages.iterpow import IPWindow
from src.pages.home import Main


class Pjmat(QMainWindow):
    def __init__(self, parent=None):
        super(Pjmat, self).__init__(parent)

        self.icon = QtGui.QIcon()
        self.icon.addPixmap(QtGui.QPixmap('src/image/bg.jpg'), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.setWindowIcon(self.icon)
        QFontDatabase.addApplicationFont('src/font/NeoEuler.ttf')

        self.uiMainWindow = Main()
        #self.uiFuel = IPWindow()
        #self.uiFp = FlightPlan()
        #self.uiDimension = Dimension()
        self.startMainWindow()

    def startMainWindow(self):
        self.uiMainWindow.setupUI(self)
        self.uiMainWindow.ipBt.clicked.connect(self.startIterPow)
        self.show()

    def startIterPow(self):
        self.uiFuel.setupUI(self)
        self.uiFuel.homeBt.clicked.connect(self.startMainWindow)
        self.uiFuel.ipbt.clicked.connect(self.startIp)
        self.show()

    


if __name__ == '__main__':
    font = QFont('aero')
    app = QApplication(sys.argv)
    app.setStyle('Window')
    app.setStyleSheet(open('./src/css/main.css').read())
    window = Pjmat()
    sys.exit(app.exec_())

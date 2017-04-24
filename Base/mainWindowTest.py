#!/usr/bin/python
import sys
from PySide import QtGui
from PySide.QtGui import QPushButton
from PySide.QtUiTools import QUiLoader


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):   
        self.setGeometry(200, 500, 400, 400)
        self.setWindowTitle("A Grid Layout")
        grid = QtGui.QGridLayout()
        self.tab = QtGui.QTabWidget()
        self.tab.setStyleSheet("QTabBar::tab { height: 35px; width: 100px; }")
        loader = QUiLoader()
        self.ui = loader.load('login.ui', self)
        self.b_search = self.ui.findChild(QPushButton, "b_login")
        self.b_search.clicked.connect(self.search)

        newTab = QtGui.QWidget()
        newTab2 = QtGui.QWidget()
        self.tab.addTab(self.ui, "Dashboard")
        self.tab.addTab(newTab2, "Patient")


        grid.setSpacing(10)
        grid.addWidget(self.tab)
        centralWidget = QtGui.QWidget()
        centralWidget.setLayout(grid)
        self.setCentralWidget(centralWidget)
        self.show()

    def search(self):
        del self.ui
        loader = QUiLoader()
        self.ui = loader.load('RoomManagerUI.ui', self)
        self.tab.addTab(self.ui, "Dash")
        self.tab.setCurrentWidget(self.ui)
        print("boss")

def main():
    app = QtGui.QApplication(sys.argv)
    win = Window()
    exit(app.exec_())


if __name__ == "__main__":
    main()

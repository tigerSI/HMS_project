import sys
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
from Base import mainRoomManager

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loader = QUiLoader()
        self.tabWidget = QTabWidget()
        self.centralWidget = QWidget()
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 500, 400, 400)
        self.setWindowTitle("MainWindow")
        self.setTab()
        grid = QGridLayout()
        grid.addWidget(self.tabWidget)
        self.centralWidget.setLayout(grid)
        self.setCentralWidget(self.centralWidget)
        self.show()

    def setTab(self):
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 35px; width: 100px; }")
        self.addNewTab()

    def addNewTab(self):
        RoomWindow = mainRoomManager.RoomWindow()
        RoomWindow.initRoomButton()
        self.connectButton(RoomWindow.allRoomButton, RoomWindow)
        ui = RoomWindow.getUi()
        self.tabWidget.addTab(ui, "Roommaneger")

    def connectButton(self, allButton, c):
        for b in allButton:
            b.clicked.connect(c.getDataOfRoom)


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    exit(app.exec_())

if __name__ == "__main__":
    main()

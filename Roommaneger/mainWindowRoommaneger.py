import sys
from PySide.QtGui import *
from PySide.QtUiTools import QUiLoader
from Roommaneger import RoomSystemClass
from Roommaneger import setting


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.loader = QUiLoader()
        self.tabWidget = QTabWidget()
        self.centralWidget = QWidget()
        self.initUI()
        self.allRoomButton = []
        self.initButtonTab1()
        self.initButtonTab2()

    def initUI(self):
        self.setGeometry(200, 500, 400, 400)
        self.setWindowTitle("Room manger")
        self.setTab()
        grid = QGridLayout()
        grid.addWidget(self.tabWidget)
        self.centralWidget.setLayout(grid)
        self.setCentralWidget(self.centralWidget)
        self.show()

    def setTab(self):
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 35px; width: 100px; }")
        self.tab1 = self.loader.load('./view/RoomManagerUI.ui', self)
        self.tab2 = self.loader.load('./view/ManageRoomForPatientUI.ui', self)
        self.tabWidget.addTab(self.tab1, "All Room")
        self.tabWidget.addTab(self.tab2, "Patient")

    def initButtonTab1(self):
        self.allRoomButton.append(self.tab1.findChild(QPushButton, "buffer"))
        for i in range(1, setting.NUMBER_OF_ROOM+1):
            name_room = "room_" + str(i)
            self.allRoomButton.append(self.tab1.findChild(QPushButton, name_room))
        self.setConnectButton()

    def initButtonTab2(self):
        pass

    def setConnectButton(self):
        self.system = RoomSystemClass.RoomSystem()
        self.allRoomButton[1].clicked.connect(lambda: self.system.getDataOfRoom(1))
        self.allRoomButton[2].clicked.connect(lambda: self.system.getDataOfRoom(2))
        self.allRoomButton[3].clicked.connect(lambda: self.system.getDataOfRoom(3))
        self.allRoomButton[4].clicked.connect(lambda: self.system.getDataOfRoom(4))
        self.allRoomButton[5].clicked.connect(lambda: self.system.getDataOfRoom(5))
        self.allRoomButton[6].clicked.connect(lambda: self.system.getDataOfRoom(6))
        self.allRoomButton[7].clicked.connect(lambda: self.system.getDataOfRoom(7))
        self.allRoomButton[8].clicked.connect(lambda: self.system.getDataOfRoom(8))
        self.allRoomButton[9].clicked.connect(lambda: self.system.getDataOfRoom(9))
        self.allRoomButton[10].clicked.connect(lambda: self.system.getDataOfRoom(10))
        self.allRoomButton[11].clicked.connect(lambda: self.system.getDataOfRoom(11))
        self.allRoomButton[12].clicked.connect(lambda: self.system.getDataOfRoom(12))
        self.allRoomButton[13].clicked.connect(lambda: self.system.getDataOfRoom(13))


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    exit(app.exec_())

if __name__ == "__main__":
    main()

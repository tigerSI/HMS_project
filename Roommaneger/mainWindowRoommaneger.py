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
        self.system = RoomSystemClass.RoomSystem()

    def initUI(self):
        self.setGeometry(200, 500, 400, 400)
        self.setWindowTitle("Roommanger")
        self.setTab()
        grid = QGridLayout()
        grid.addWidget(self.tabWidget)
        self.centralWidget.setLayout(grid)
        self.setCentralWidget(self.centralWidget)
        self.show()

    def setTab(self):
        self.tabWidget.setStyleSheet("QTabBar::tab { height: 35px; width: 100px; }")
        self.tab1 = self.loader.load('./RoomManagerUI.ui', self)
        self.tab2 = self.loader.load('./view/ManageRoomForPatientUI.ui', self)
        self.tabWidget.addTab(self.tab1, "All Room")
        self.tabWidget.addTab(self.tab2, "Patient")

    def initButtonTab1(self):
        self.allRoomButton.append(self.tab1.findChild(QPushButton, "buffer"))
        for i in range(1, setting.NUMBER_OF_ROOM):
            name_room = "room_" + str(i)
            self.allRoomButton.append(self.tab1.findChild(QPushButton, name_room))
            self.allRoomButton[i].clicked.connect(self.getDataOfRoom)

    def getDataOfRoom(self):
        for room in self.system.allRoom:
            if room.number == int(self.sender().text()):
                print("yeah")

def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    exit(app.exec_())

if __name__ == "__main__":
    main()

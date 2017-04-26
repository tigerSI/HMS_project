import sys
from Roommaneger import RoomSystemClass
from Roommaneger import RoomClass
from Roommaneger import setting
from PySide.QtGui import *
from PySide.QtUiTools import *


class RoomWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        loader = QUiLoader()
        self.ui = loader.load('tab1_all_room.ui', self)
        self.layout = QGridLayout()
        self.layout.addWidget(self.ui)
        self.allRoomButton = []
        self.initRoomButton()
        self.system = RoomSystemClass.RoomSystem()

    def getUi(self):
        return self.ui

    def initRoomButton(self):
        print("init ")
        self.allRoomButton.append(self.ui.findChild(QPushButton, "buffer"))
        for i in range(1, setting.NUMBER_OF_ROOM):
            name_room = "room_" + str(i)
            self.allRoomButton.append(self.ui.findChild(QPushButton, name_room))
            self.allRoomButton[i].clicked.connect(self.getDataOfRoom)

    def getDataOfRoom(self):
        print("in")
        for room in self.system.allRoom:
            if room.number == int(self.sender().text()):
                print("yeah")


global w
def main():
    app = QApplication(sys.argv)
    w = RoomWindow()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
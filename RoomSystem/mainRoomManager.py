import sys
from RoomSystem import RoomSystem1
from RoomSystem import RoomClass
from RoomSystem import setting
from PySide.QtGui import *
from PySide.QtUiTools import *


class RoomWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        loader = QUiLoader()
        self.ui = loader.load('RoomManagerUI.ui', self)
        self.setCentralWidget(self.ui)
        self.allRoomButton = []
        self.initRoomButton()
        self.system = RoomSystem1.RoomSystem()

    def initRoomButton(self):
        self.allRoomButton.append(self.ui.findChild(QPushButton, "buffer"))
        for i in range(1, setting.NUMBER_OF_ROOM):
            name_room = "room_" + str(i)
            self.allRoomButton.append(self.ui.findChild(QPushButton, name_room))
            self.allRoomButton[i].clicked.connect(self.getDataOfRoom)

    def getDataOfRoom(self):
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
import sys
from RoomSystem import setting
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtUiTools import *


class RoomWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)
        loader = QUiLoader()
        self.ui = loader.load('RoomManagerUI.ui', self)
        self.setCentralWidget(self.ui)
        self.allRoomButton = []

    def initRoomButton(self):
        for i in range(setting.NUMBER_OF_ROOM):
            name_room = "room_" + str(i)
            self.allRoomButton[i] = self.ui.findChild(QPushButton, name_room)
            self.allRoomButton[i].clicked.connect(self.getDataOfRoom)

    def getDataOfRoom(self):
        print("boss")

global w
def main():
    app = QApplication(sys.argv)
    w = RoomWindow()
    w.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
from PySide.QtGui import QMessageBox

from Employee.Roommanager import RoomClass


class RoomSystem:
    def __init__(self):
        self.numberOfRoom = 13
        self.allRoom = []
        self.initRoom()

    def initRoom(self):
        for i in range(self.numberOfRoom):
            self.allRoom.append(RoomClass.Room(i, 0))

    def getInfo(self, num):
        data = []
        for name in self.allRoom[num].allPatient:
            data.append(name)
        return data

    def getDataOfRoom(self, nRoom):
        text = "All Patient" + "\n"
        text += "\tAtichat L." + "\n" +"\tSirapop S." + "\n" + "\tNuttera N."
        self.getMsgBox(text, nRoom)

    def getMsgBox(self, text, nRoom):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Room: " + str(nRoom))
        msgBox.setText(text)
        msgBox.addButton(QMessageBox.Ok)
        msgBox.show()
        msgBox.exec_()




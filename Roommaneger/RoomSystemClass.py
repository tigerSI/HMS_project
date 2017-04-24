from Roommaneger import RoomClass
from Roommaneger import setting


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
from items import *


class RoomGeneral:
    def __init__(self):
        self.description = "You are in a room"
        self.north_door = False
        self.south_door = False
        self.east_door = False
        self.west_door = False
        self.items = []

class Room0(RoomGeneral):
    def __init__(self):
        super().__init__()  # Used when a class grabs a class
        self.description = "There is a number painted in the walls saying 'Zero'. You see a door to the east and a door to the north."
        self.east_door = Room1()
        self.north_door = Room2()
        self.items = [Key1(), Paper1()]


class Room1(RoomGeneral):
    def __init__(self):
        super().__init__()
        self.description = "There is a number painted in the walls saying 'One'."
        self.items = ['Room 2 Key']
import random
import math

def get_room_description(room_number):
    if room_number == 0:
        description = "Room 0 description"
    elif room_number == 1:
        description = "Room 1 description"
    elif room_number == 2:
        description = "Room 2 description"
    elif room_number == 3:
        description = "Room 3 description"
    elif room_number == 4:
        description = "Room 4 description"
    elif room_number == 5:
        description = "Room 5 description"
    elif room_number == 6:
        description = "Room 6 description"
    else:
        print('ERROR room not found, cannot describe room.')
    return description


# Room inventory: what rooms have
room0_inventory = ['acid','paper', 'keys']
room1_inventory = ['x','y', 'z']
room2_inventory = ['a','b', 'c']
room3_inventory = ['d','e', 'f']
room4_inventory = ['g','h', 'i']
room5_inventory = ['j','k', 'l']
room6_inventory = ['m','n', 'o']


room_inventory_list = [room0_inventory, room1_inventory, room2_inventory, room3_inventory,
                       room4_inventory, room5_inventory, room6_inventory]



# Room connections: how rooms are connected
# North = 1
# South = 2
# East = 3
# West = 4
# room_connections = [north, south, east, west]
def get_room_connections(room_number):
    if room_number == 0:
        return [1, None, 3, 4]
    elif room_number == 1:
        return [None, 2, None, 4]
    elif room_number == 2:
        return [None, None, None, None]
    elif room_number == 3:
        return [None, None, None, None]
    elif room_number == 4:
        return [None, None, None, None]
    elif room_number == 5:
        return [None, None, None, None]
    elif room_number == 6:
        return [None, None, None, None]
# Note to self: Make a map and define room layouts

def room_travel(destination:int, current_room:int):
    if destination in get_room_connections(current_room):
        return destination
    else:
        print("You cannot go there silly!")
        return current_room


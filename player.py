import random
import math
from room import *

inventory = []
def player_inventory():

    return inventory

def add_item_to_inventory(item_name, current_room):
    if item_name in room_inventory_list[current_room]:
        inventory.append(item_name)
        room_inventory_list[current_room].remove(item_name)
    else:
        print(f'The item \"{item_name}\" does not exit in the room...')
    return



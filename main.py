import math
import random

from player import *
from room import *


def main():

    game_loop = True
    player_name = input("What will your character's name be?: ")
    print(f"Welcome {player_name}!")
    print("Instructions")  # have to do this

    current_room = 0  # zero as in room zero

    while game_loop:
        player_action = input("What would you like to do?: ")
        input_list = player_action.split()
        player_command = input_list[0].lower()
        if player_command == 'look':
            print(get_room_description(current_room))

        elif player_command == 'inventory':
            print(player_inventory())

        elif player_command == 'help':
            print('Really bro? pay more attention next time.\nInstructions')
            # Write out game instructions/guidelines

        elif player_command == 'get':
            if input_list[1].lower() in room_inventory_list[current_room]:  # Room items
                add_item_to_inventory(input_list[1].lower(), current_room)  # Item names must be 1 word
                print(f'You have acquired \"{input_list[1].lower()}\"!\nIt has been added to your inventory.')

        elif player_command == 'use':
            x = 'WORK ON THIS'
            # Define the game ide and the items we will need

        elif player_command == 'go':
            if input_list[1].lower() == 'north':
                current_room = room_travel(0, current_room)
            elif input_list[1].lower() == 'south':
                current_room = room_travel(1, current_room)
            elif input_list[1].lower() == 'east':
                current_room = room_travel(2, current_room)
            elif input_list[1].lower() == 'west':
                current_room = room_travel(3, current_room)


if __name__ == '__main__':
    main()

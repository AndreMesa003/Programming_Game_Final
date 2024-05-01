import math
import random

import room
from player import *
from room import *


def main():

    game_loop = True
    player = Player()
    print(f"Your name is {player.name} !")
    print("Instructions") # have to do this

    current_room = Room0()
    while game_loop == True:
        act = input("What would you like to do?: ")
        input_list = act.split()
        if input_list[0].lower() == 'look':
            print(current_room.description)

        elif input_list[0].lower() == 'inventory':
            print(player.inventory)

        elif input_list[1].lower() == 'inspect'

        elif input_list[0].lower() == 'help':
            # Write out game instructions/guidelines

        elif input_list[0].lower() == 'get':
            if input_list[1].lower() in current_room.items.lower():
                player.inventory.append(input_list[1])

        elif input_list[0].lower() == 'go':
            if input_list[1].lower() in ['north','south','east','west']:
                if


if __name__ == '__main__':
    main()




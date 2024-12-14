# Victor Zuniga Salgado

def main_menu():
    # Introduction and instructions for game
    print("Battle at Mystery Manor Text Adventure Game")
    print("Collect 6 items to win the game, or be killed by the evil wizard.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


def move_between_rooms(current_room, move, rooms):
    # move to corresponding room
    current_room = rooms[current_room][move]
    return current_room


def get_item(current_room, move, rooms, inventory):
    # Add item to the players inventory
    inventory.append(rooms[current_room]['item'])
    del rooms[current_room]['item']


def main():
    # Dictionary of linking one room to another as well as the item found in each room
    rooms = {
        'Star Hallway': {'South': 'Bathroom', 'North': 'Bedroom', 'East': 'War Room', 'West': 'Wine Room'},
        'Bathroom': {'North': 'Star Hallway', 'East': 'Kitchen', 'item': 'Potion'},
        'Kitchen': {'West': 'Bathroom', 'item': 'Pizza Slice'},
        'Bedroom': {'South': 'Star Hallway', 'East': 'Makeup Room', 'item': 'Running Shoes'},
        'Makeup Room': {'West': 'Bedroom', 'item': 'Hand Mirror'},
        'Wine Room': {'East': 'Star Hallway', 'item': 'Armor'},
        'War Room': {'West': 'Star Hallway', 'North': 'Library', 'item': 'Sword'},
        'Library': ''
    }
    s = ' '
    # list for storing player inventory
    inventory = []
    # start room
    current_room = "Star Hallway"
    # show the player the main menu
    main_menu()

    while True:
        # Player finds the evil wizard
        if current_room == 'Library':
            # The player wins the game
            if len(inventory) == 6:
                print('You see the evil wizard! KERPLUNK… THE DAY IS SAVED!')
                print('Thanks for playing the game! Hope you enjoyed it!')
                break
            # The player loses the game
            else:
                print('\nOH NO! Unfortunately, You did not collect all of the items!')
                print('The evil wizard has crashed your party and the manor was destroyed!')
                print('Thanks for playing the game! Hope you enjoyed it!')
                break
        # Tell the player the current room & inventory, and tell them to select next move
        print('You are in the ' + current_room)
        print(inventory)
        # Tell the player what item is currently in the room
        if current_room != 'Library' and 'item' in rooms[current_room].keys():
            print('You see the {}'.format(rooms[current_room]['item']))
        print('------------------------------')
        move = input('Enter your move: ').title().split()

        # Player wants to enter another room
        if len(move) >= 2 and move[1] in rooms[current_room].keys():
            current_room = move_between_rooms(current_room, move[1], rooms)
            continue
        # Player decides to pick up item in room
        elif len(move[0]) == 3 and move[0] == 'Get' and ' '.join(move[1:]) in rooms[current_room]['item']:
            print('You pick up the {}'.format(rooms[current_room]['item']))
            print('------------------------------')
            get_item(current_room, move, rooms, inventory)
            continue
        # Player enters an invalid command
        else:
            print('Invalid move, please try again')
            continue


main()
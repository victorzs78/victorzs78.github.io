import random

def main_menu():
    print("Welcome to Battle at Mystery Manor Text Adventure Game!")
    print("Collect 6 items to win the game, or beware of the evil wizard!")
    print("Commands:")
    print(" - Move: go South, go North, go East, go West")
    print(" - Pick up an item: get 'item name'")
    print(" - Drop an item: drop 'item name'")
    print(" - Examine the room: examine")
    print(" - Check inventory: inventory")

def move_between_rooms(current_room, move, rooms):
    if move in rooms[current_room]:
        current_room = rooms[current_room][move]
    else:
        print("You can't go that way.")
    return current_room

def get_item(current_room, inventory, rooms):
    if 'item' in rooms[current_room]:
        item = rooms[current_room]['item']
        if len(inventory) < 4:  # inventory size limit
            inventory.append(item)
            print(f"You picked up: {item}")
            del rooms[current_room]['item']
        else:
            print("Your inventory is full! Drop an item before picking up a new one.")
    else:
        print("There is no item to pick up here.")

def drop_item(item_name, inventory, current_room, rooms):
    if item_name in inventory:
        inventory.remove(item_name)
        rooms[current_room]['item'] = item_name
        print(f"You dropped: {item_name}")
    else:
        print("You don't have that item in your inventory.")

def examine_room(current_room, rooms):
    print(f"You are in the {current_room}. {rooms[current_room].get('description', 'It\'s a mysterious place.')}")
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}.")

def main():
    rooms = {
        'Star Hallway': {'South': 'Bathroom', 'North': 'Bedroom', 'East': 'War Room', 'West': 'Wine Room', 'description': 'A grand hallway with starlit chandeliers.'},
        'Bathroom': {'North': 'Star Hallway', 'East': 'Kitchen', 'item': 'Potion', 'description': 'A bathroom with marble floors and a mysterious mist.'},
        'Kitchen': {'West': 'Bathroom', 'item': 'Pizza Slice', 'description': 'A kitchen filled with the aroma of fresh herbs and spices.'},
        'Bedroom': {'South': 'Star Hallway', 'East': 'Makeup Room', 'item': 'Running Shoes', 'description': 'A cozy bedroom with a warm fireplace.'},
        'Makeup Room': {'West': 'Bedroom', 'item': 'Hand Mirror', 'description': 'A room filled with vanity mirrors and vintage perfumes.'},
        'Wine Room': {'East': 'Star Hallway', 'item': 'Armor', 'description': 'A dimly lit room lined with ancient wine bottles.'},
        'War Room': {'West': 'Star Hallway', 'North': 'Library', 'item': 'Sword', 'description': 'An armory with swords, shields, and suits of armor.'},
        'Library': {'description': 'A dark and quiet library, filled with ancient books.'}
    }

    inventory = []
    current_room = "Star Hallway"
    main_menu()

    while True:
        print(f"\nYou are in the {current_room}.")
        action = input("Enter your action: ").strip().lower().split()

        if action[0] == "go" and len(action) > 1:
            direction = action[1].capitalize()
            current_room = move_between_rooms(current_room, direction, rooms)
            
            # Random chance of encountering the wizard
            if random.random() < 0.2 and current_room != 'Library':
                print("You encounter the evil wizard!")
                if len(inventory) == 6:
                    print("You use all your items to defeat the wizard! You win!")
                    break
                else:
                    print("You were unprepared and the wizard has defeated you. Game Over.")
                    break
        elif action[0] == "get" and len(action) > 1:
            item_name = " ".join(action[1:]).title()
            get_item(current_room, inventory, rooms)
        elif action[0] == "drop" and len(action) > 1:
            item_name = " ".join(action[1:]).title()
            drop_item(item_name, inventory, current_room, rooms)
        elif action[0] == "examine":
            examine_room(current_room, rooms)
        elif action[0] == "inventory":
            print("Inventory:", inventory)
        elif current_room == "Library":
            if len(inventory) == 6:
                print("You've gathered all items and defeated the wizard in the library. You win!")
            else:
                print("The evil wizard appears and you've failed to collect all items. Game Over.")
            break
        else:
            print("Invalid command.")

main()

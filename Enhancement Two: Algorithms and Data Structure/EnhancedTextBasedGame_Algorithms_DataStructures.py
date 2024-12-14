import random
import heapq
from collections import deque

# Room class for graph representation
class Room:
    def __init__(self, name, description, item=None):
        self.name = name
        self.description = description
        self.item = item
        self.neighbors = {}  # Neighboring rooms (connections)
        self.item_history = deque()  # Linked list for item history in this room

    def add_neighbor(self, direction, neighbor):
        self.neighbors[direction] = neighbor

    def show_item_history(self):
        # Display the history of items in the room
        if self.item_history:
            print(f"Item history in {self.name}: {list(self.item_history)}")
        else:
            print(f"No items have been dropped or picked up in {self.name}.")

# Graph class for managing rooms
class RoomGraph:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room_name, description, item=None):
        room = Room(room_name, description, item)
        self.rooms[room_name] = room
        return room

    def connect_rooms(self, room1_name, room2_name, direction):
        room1 = self.rooms[room1_name]
        room2 = self.rooms[room2_name]
        room1.add_neighbor(direction, room2)
        # Create two-way connections
        reverse_direction = {"North": "South", "South": "North", "East": "West", "West": "East"}
        room2.add_neighbor(reverse_direction[direction], room1)

    def shortest_path(self, start_name, goal_name):
        queue = deque([(start_name, [start_name])])
        visited = set()
        while queue:
            current, path = queue.popleft()
            if current == goal_name:
                return path
            visited.add(current)
            for neighbor in self.rooms[current].neighbors.values():
                if neighbor.name not in visited:
                    queue.append((neighbor.name, path + [neighbor.name]))
        return []
    
event_queue = []

# Initialize game map with rooms and connections
game_map = RoomGraph()
game_map.add_room('Star Hallway', 'A grand hallway with starlit chandeliers.')
game_map.add_room('Bathroom', 'A bathroom with marble floors and a mysterious mist.', 'Potion')
game_map.add_room('Kitchen', 'A kitchen filled with the aroma of fresh herbs and spices.', 'Pizza Slice')
game_map.add_room('Bedroom', 'A cozy bedroom with a warm fireplace.', 'Running Shoes')
game_map.add_room('Makeup Room', 'A room filled with vanity mirrors and vintage perfumes.', 'Hand Mirror')
game_map.add_room('Wine Room', 'A dimly lit room lined with ancient wine bottles.', 'Armor')
game_map.add_room('War Room', 'An armory with swords, shields, and suits of armor.', 'Sword')
game_map.add_room('Library', 'A dark and quiet library, filled with ancient books.')

game_map.connect_rooms('Star Hallway', 'Bathroom', 'South')
game_map.connect_rooms('Star Hallway', 'Bedroom', 'North')
game_map.connect_rooms('Star Hallway', 'War Room', 'East')
game_map.connect_rooms('Star Hallway', 'Wine Room', 'West')
game_map.connect_rooms('Bathroom', 'Kitchen', 'East')
game_map.connect_rooms('Bedroom', 'Makeup Room', 'East')
game_map.connect_rooms('War Room', 'Library', 'North')

inventory = set()

def main_menu():
    print("Welcome to Battle at Mystery Manor Text Adventure Game!")
    print("Collect 6 items to win the game, or beware of the evil wizard!")
    print("Commands:")
    print(" - Move: go South, go North, go East, go West")
    print(" - Pick up an item: get 'item name'")
    print(" - Drop an item: drop 'item name'")
    print(" - Examine the room: examine")
    print(" - Check inventory: inventory")
    print(" - Find path to Library: path")
    print(" - View room item history: history")

def move_between_rooms(current_room, direction):
    if direction in current_room.neighbors:
        return current_room.neighbors[direction]
    else:
        print("You can't go that way.")
        return current_room

def get_item(current_room):
    if current_room.item:
        if len(inventory) < 6:
            inventory.add(current_room.item)
            print(f"You picked up: {current_room.item}")
            current_room.item_history.append(f"Picked up {current_room.item}")
            current_room.item = None
        else:
            print("Your inventory is full!")
    else:
        print("There is no item to pick up here.")

def drop_item(item_name, current_room):
    if item_name in inventory:
        inventory.remove(item_name)
        current_room.item = item_name
        current_room.item_history.append(f"Dropped {item_name}")
        print(f"You dropped: {item_name}")
    else:
        print("You don't have that item in your inventory.")

def examine_room(current_room):
    print(f"You are in the {current_room.name}. {current_room.description}")
    if current_room.item:
        print(f"You see a {current_room.item}.")

def handle_event():
    if event_queue:
        priority, event = heapq.heappop(event_queue)
        if event == "wizard encounter":
            print("You encounter the evil wizard!")
            if len(inventory) == 6:
                print("You use all your items to defeat the wizard! You win!")
                return True
            else:
                print("You were unprepared and the wizard has defeated you. Game Over.")
                return True
    return False

def main():
    current_room = game_map.rooms['Star Hallway']
    main_menu()

    while True:
        print(f"\nYou are in the {current_room.name}.")
        action = input("Enter your action: ").strip().lower().split()

        if action[0] == "go" and len(action) > 1:
            direction = action[1].capitalize()
            current_room = move_between_rooms(current_room, direction)
        elif action[0] == "get":
            get_item(current_room)
        elif action[0] == "drop" and len(action) > 1:
            item_name = " ".join(action[1:]).title()
            drop_item(item_name, current_room)
        elif action[0] == "examine":
            examine_room(current_room)
        elif action[0] == "inventory":
            print("Inventory:", list(inventory))
        elif action[0] == "path":
            path = game_map.shortest_path(current_room.name, "Library")
            print("Shortest path to Library:", " -> ".join(path))
        elif action[0] == "history":
            current_room.show_item_history()
        elif current_room.name == "Library":
            if len(inventory) == 6:
                print("You've gathered all items and defeated the wizard in the library. You win!")
            else:
                print("The evil wizard appears and you've failed to collect all items. Game Over.")
            break
        else:
            print("Invalid command.")

main()
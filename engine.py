import characters
import draw
import prompt
import Locations.coord_0_0 as coord_0_0

# Initialize the class:
you = characters.Player()

# Set starting location (may later be randomized):
you.location = coord_0_0.room_1

def examine(object): # In the future this function should examine more stuff.
    draw.frame(
        width = 100,
        contents = [object.description],
    )

def gameplay_loop():
    examine(you.location)
    while you.are_alive:
        what_you_do = prompt.open_response( 
            question = "What do you do?",            
            # Since prompt.open_response selects the last valid match, make sure more common options come after less common ones.
            options = [
                "drop",
                "take", "pick up", "grab",
                "examine", "look",
                "go to", "go",
            ],
        )
        match what_you_do:
            case "go" | "go to":
                go_to()
            case "examine" | "look":
                look_at()
            case "take" | "pick up" | "grab":
                pick_up()
            case "drop":
                drop()

def go_to():
    """Ask the player where they want to go. Then change their location to be the destination."""
    target = prompt.multiple_choice(
        question = "Where do you want to go?",
        options = [room.name for room in you.location.accessible_rooms],
    )
    you.location = match_string_to_class(target, you.location.accessible_rooms)
    examine(you.location)

def look_at():
    """The player can choose to look at:
        themselves, 
        the room, 
        their items, 
        the items in the room, 
        ... (more as I need)
    Those options are not presented to the player."""
    themselves = ["Self", "Me", "Myself", you.name]
    the_room = ["Room", "Area", "Here", you.location.name]
    their_items = [item.name for item in you.inventory]
    the_items_in_the_room = [item.name for item in you.location.contents]
    target = prompt.open_response(
        question = "What do you want to look at?",
        options = themselves + the_room + their_items + the_items_in_the_room,
    )
    if target in themselves:
        you.character_sheet()
    elif target in the_room:
        examine(you.location)
    elif target in their_items:
        examine(match_string_to_class(target, you.inventory))
    elif target in the_items_in_the_room:
        # examine(match_string_to_class(target, you.location.contents).description)
        examine(match_string_to_class(target, you.location.contents))

def match_string_to_class(string, list):
    """Takes a string and a list of classes. Outputs the class that has that string as its name."""
    for object in list:
        if string != object.name:
            continue
        else:
            output = object
            break
    return output

def pick_up():
    """The player takes an item from the room and adds it to their inventory."""
    target = prompt.open_response(
        question = "What do you want to pick up?",
        options = [item.name for item in you.location.contents],
    )
    item = match_string_to_class(target, you.location.contents)
    you.location.contents.remove(item)
    you.inventory.append(item)
    print(f"\nYou pick up the {item.name}.")

def drop():
    """The player chooses an item from their inventory and "drops it;" i.e., adds it to the room's contents."""
    list_of_items = []
    if you.inventory != []:
        list_of_items = [item.name for item in you.inventory]
    target = prompt.multiple_choice(
        question = "What do you want to drop?",
        options = ["Nothing"] + list_of_items,
    )
    if target != "Nothing":
        item = match_string_to_class(target, you.inventory)
        you.inventory.remove(item)
        you.location.contents.append(item)
        print(f"\nYou drop the {item.name}.")
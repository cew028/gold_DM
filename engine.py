import player
import draw
import prompt
import Locations.coord_0_0 as coord_0_0

# Initialize the class:
you = player.Player()

# Set starting location (may later be randomized):
you.location = coord_0_0.room_1

no_list = ["N", "No", "Not", "Nothing", "Quit", "Go back", "Cancel", "Abort", "Negate",] # Use this list in open_response options as a collection of responses to indicate no.

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
        unequip_and = ""
        if item.equipped == True:
            truncated_name = item.name.rsplit(" (", 1)[0]
            item.name = truncated_name
            item.equipped = False
            you.equipped_items.remove(item)
            unequip_and = "unequip and "
        you.inventory.remove(item)
        you.location.item_contents.append(item)
        print(f"\nYou {unequip_and}drop the {item.name}.")

def equip():
    """The player chooses an item from their inventory and equips it."""
    list_of_items = []
    if you.inventory != []:
        list_of_items = [item.name for item in you.inventory]
    # Remove objects you're already equipping:
    for item in you.equipped_items:
        if item.name in list_of_items:
            list_of_items.remove(item.name)
    target = prompt.multiple_choice(
        question = "What do you want to equip?",
        options = ["Nothing"] + list_of_items,
    )
    if target != "Nothing":
        item = match_string_to_class(target, you.inventory)
        # First check that it can be equipped:
        equippable = any(
            [
                item.holdable_dominant_hand,
                item.holdable_off_hand,
                item.wearable_head,
                item.wearable_torso,
                item.wearable_legs,
                item.wearable_feet,
                item.wearable_dominant_hand,
                item.wearable_off_hand,
            ]
        )
        if equippable == True:
            # Equip the item, with the following priority hierarchy:
            if item.holdable_off_hand and you.held_off_hand == None: # Off hand before dominant to dual wield shields (can't dual wield weapons as of now).
                item.name += " (Off hand)"
                you.held_off_hand = item
                item.equipped = True
                you.equipped_items.append(item) 
            elif item.holdable_dominant_hand and you.held_dominant_hand == None:
                item.name += " (Dominant hand)"
                you.held_dominant_hand = item
                item.equipped = True
                you.equipped_items.append(item) 
            elif item.wearable_torso and you.worn_torso == None:
                item.name += " (Torso)"
                you.worn_torso = item
                item.equipped = True
                you.equipped_items.append(item) 
            elif item.wearable_legs and you.worn_legs == None:
                item.name += " (Legs)"
                you.worn_legs = item
                item.equipped = True
                you.equipped_items.append(item) 
            elif item.wearable_head and you.worn_head == None:
                item.name += " (Head)"
                you.worn_head = item
                item.equipped = True
                you.equipped_items.append(item) 
            elif item.wearable_feet and you.worn_feet == None:
                item.name += " (Feet)"
                you.worn_feet = item
                item.equipped = True
                you.equipped_items.append(item) 
            elif item.wearable_dominant_hand and you.worn_dominant_hand == None: # Dominant hand before off hand for wearing
                item.name += " (Dominant hand)"
                you.worn_dominant_hand = item
                item.equipped = True
                you.equipped_items.append(item) 
            elif item.wearable_off_hand and you.worn_off_hand == None:
                item.name += " (Off hand)"
                you.worn_off_hand = item
                item.equipped = True
                you.equipped_items.append(item) 
            else:
                print(f"You can't equip the {item.name}, since you're already equipping something in its place.")
        else:
            print(f"The {item.name} is not equippable.")

def examine(object):
    draw.frame(
        width = 100,
        contents = [object.description],
    )

def gameplay_loop():
    examine(you.location)
    while you.are_alive:
        what_you_do = prompt.open_response( 
            question = "What do you do?",            
            # Fill out the options with as many synonyms as possible.
            # For readability, put synonyms on the same line.
            # Since open_response outputs the last selected option, substrings need to come first.
            # For example: "equip" needs to come before "unequip". "move" needs to come before "remove".
            options = [
                "go", "move", "walk", "run", "flee", "escape",
                "equip", "wear", "put on",
                "unequip", "remove", "take off",
                "drop", "put down", "place",
                "take", "pick up", "grab",
                "examine", "look", "look at",
            ],
        )
        match what_you_do:
            case "go" | "move" | "walk" | "run" | "flee" | "escape":
                go_to()
            case "examine" | "look" | "look at":
                look_at()
            case "take" | "pick up" | "grab":
                pick_up()
            case "drop" | "put down" | "place":
                drop()
            case "equip" | "wear" | "put on":
                equip()
            case "unequip" | "remove" | "take off":
                unequip()

def go_to():
    """Ask the player where they want to go. Then change their location to be the destination."""
    target = prompt.multiple_choice(
        question = "Where do you want to go?",
        options = ["Here"] + [room.name for room in you.location.accessible_rooms],
    )
    if target != "Here":
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
    the_items_in_the_room = [item.name for item in you.location.item_contents]
    target = prompt.open_response(
        question = "What do you want to look at?",
        options = no_list + themselves + the_room + their_items + the_items_in_the_room,
    )
    if target in themselves:
        you.character_sheet()
    elif target in the_room:
        examine(you.location)
    elif target in their_items:
        examine(match_string_to_class(target, you.inventory))
    elif target in the_items_in_the_room:
        examine(match_string_to_class(target, you.location.item_contents))
    elif target in no_list:
        print("\nYou canceled.")

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
        options = no_list + [item.name for item in you.location.item_contents],
    )
    if target not in no_list:
        item = match_string_to_class(target, you.location.item_contents)
        you.location.item_contents.remove(item)
        you.inventory.append(item)
        print(f"\nYou pick up the {item.name}.")
    else:
        print("\nYou canceled.")

def unequip():
    """The player chooses an item they are currently equipping and unequips it."""
    list_of_items = []
    if you.equipped_items != []:
        list_of_items = [item.name for item in you.equipped_items]
    target = prompt.multiple_choice(
        question = "What do you want to unequip?",
        options = ["Nothing"] + list_of_items,
    )
    if target != "Nothing":
        item = match_string_to_class(target, you.inventory)
        you.equipped_items.remove(item)
        if you.held_off_hand == item:
            you.held_off_hand = None
        if you.held_dominant_hand == item:
            you.held_dominant_hand = None
        if you.worn_torso == item:
            you.worn_torso = None
        if you.worn_legs == item:
            you.worn_legs = None
        if you.worn_head == item:
            you.worn_head = None
        if you.worn_feet == item:
            you.worn_feet = None
        if you.worn_dominant_hand == item:
            you.worn_dominant_hand = None
        if you.worn_off_hand == item:
            you.worn_off_hand = None
        # Delete the text indicating where the item is equipped:
        truncated_name = item.name.rsplit(" (", 1)[0]
        item.name = truncated_name
        print(f"\nYou unequip the {item.name}.")
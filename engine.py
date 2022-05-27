import characters
import draw
import prompt
import Locations.coord_0_0 as coord_0_0

# Initialize the class:
you = characters.Player()

# Set starting location (may later be randomized):
you.location = coord_0_0.room_1

def examine(room): # In the future this function should examine more stuff.
    print(room.description)

def gameplay_loop():
    while you.are_alive:        
        draw.frame(
            width = 100,
            contents = [you.location.description],
        )
        what_you_do = prompt.open_response(
            question = "What do you do?",
            options = [
                "go",
                "go to",
            ],
        )
        match what_you_do:
            case "go" | "go to":
                go_to()

def go_to():
    """Ask the player where they want to go. Then change their location to be the destination."""
    target = prompt.multiple_choice(
        question = "Where do you want to go?",
        options = [room.name for room in you.location.accessible_rooms],
    )
    for room in you.location.accessible_rooms:
        if target != room.name:
            continue
        else:
            destination = room
            break
    you.location = destination
import characters
import draw
import prompt
import Locations.coord_0_0 as coord_0_0
import Locations.room_manager as room_manager

you = characters.Player()

you.location = coord_0_0.room_1

def gameplay_loop():
    draw.frame(
        width = 100,
        contents = [you.location.description],
    )
    while you.are_alive:
        what_you_do = prompt.open_response(
            question = "What do you do?",
            options = [
                "go",
                "go to",
            ],
        )
        match what_you_do:
            case "go" | "go to":
                navigate()

def navigate():
    destination = prompt.multiple_choice(
        question = "Where do you want to go?",
        options = you.location.accessible_rooms,
    )
    room_manager.go_from_a_to_b(you.location, destination)
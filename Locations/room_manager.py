class Room():
    def __init__(
        self,
        name = "No name",
        description = "No description",
        accessible_rooms = [],
    ):
        self.name = name
        self.description = description
        self.accessible_rooms = accessible_rooms

def examine(room):
    print(room.description)

def go_from_a_to_b(source, target):
    """Input a source room and a target room. If the target is in the source's list of accessible_rooms, go to that room."""
    # Eventually when I add new world map coordinates this function should also update to be able to travel between coordinates.
    if target in source.accessible_rooms:
        print(f"TODO: You go to room {target}")
    else:
        print("TODO: You can't go there.")

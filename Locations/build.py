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
    
    def go_to(self, room):
        """Input a room. If the room is in the list of accessible_rooms, go to that room."""
        if room in self.accessible_rooms:
            print(f"TODO: You go to room {room}")
        else:
            print("TODO: You can't go there.")
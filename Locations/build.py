class Room():
    def __init__(
        self,
        name = "No name",
        description = "No description",
        accessible_rooms = [],
        item_contents = [],
    ):
        self.name = name
        self.description = description
        self.accessible_rooms = accessible_rooms
        self.item_contents = item_contents
import Locations.build as build

details = {
    "Coordinates" : (0, 0),
    "Module" : "Tomb of the Serpent Kings",
    "Number of rooms" : 52,
    "Arrival text" : "Blah"
}

room_1 = build.Room(
    name = "1: ENTRANCE HALL",
    description = "A long corridor with four open rooms, two on either side. The hallway ends at a large, barred door made of stone, leading to 6: FALSE KING’S TOMB.",
    accessible_rooms = ["2: GUARD TOMBS", "3: SCHOLAR TOMB", "4: SORCERER TOMB", "5: DOOR/HAMMER TRAP"],
)
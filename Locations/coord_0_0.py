import Locations.room_manager as room_manager

details = {
    "Coordinates" : (0, 0),
    "Module" : "Tomb of the Serpent Kings",
    "Number of rooms" : 52,
    "Arrival text" : "Blah"
}

room_1 = room_manager.Room(
    name = "1: ENTRANCE HALL",
    description = "A long corridor with four open rooms, two on either side. The hallway ends at a large, barred door made of stone, leading to 6: FALSE KING’S TOMB.",
    accessible_rooms = ["2: GUARD TOMBS", "3: SCHOLAR TOMB", "4: SORCERER TOMB", "5: DOOR/HAMMER TRAP"],
)

room_2 = room_manager.Room(
    name = "2: GUARD TOMBS",
    description = "These small rooms are identical in size and content. They both contain a wooden coffin with a clay statue of a snake-man warrior inside. The statues are hollow. Each contains a gold amulet worth 1gp, a dried snake skeleton, and a cloud of poison gas (d6 damage, can only reduce a PC to 0 HP).",
    accessible_rooms = ["1: ENTRANCE HALL"],
)

room_3 = room_manager.Room(
    name = "3: SCHOLAR TOMB",
    description = "Similar to 2: GUARD TOMBS, but inside the coffin is a clay statue of a thin and sly-looking snake-man scholar. Its scrolls have crumbled to dust. The statue contains the same amulet, snake skeleton, and poison as the others.",
    accessible_rooms = ["1: ENTRANCE HALL"],
)

room_4 = room_manager.Room(
    name = "4: SORCERER TOMB",
    description = "Similar to 2: GUARD TOMBS, but inside the coffin there is a clay statue of a robed snake-man sorcerer wearing a silver ring. If the PCs didn’t already learn that the other statues were hollow, they’ll almost certainly try to pry the ring off, breaking the statue open and revealing the poison gas and amulet. The ring is a magical, but also cursed. If worn on a finger, the fingernail becomes long, bifurcated, and pointed like twin fangs. It can be used like a poison dagger (living targets must Save vs. Poison or take +1d6 poison damage on a hit), but each morning, the wearer must Save vs. Poison or take d6 damage. If they take 6 damage at once from the poison ring, their finger falls off and turns into a snake.",
    accessible_rooms = ["1: ENTRANCE HALL"],
)

room_5 = room_manager.Room(
    name = "5: DOOR/HAMMER TRAP",
    description = "Blah blah ",
    accessible_rooms = ["1: ENTRANCE HALL", "6: FALSE KING'S TOMB"],
)
import Items.craft as craft
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
)

room_2 = build.Room(
    name = "2: GUARD TOMBS",
    description = "These small rooms are identical in size and content. They both contain a wooden coffin with a clay statue of a snake-man warrior inside. The statues are hollow. Each contains a gold amulet worth 1gp, a dried snake skeleton, and a cloud of poison gas (d6 damage, can only reduce a PC to 0 HP).",
)

room_3 = build.Room(
    name = "3: SCHOLAR TOMB",
    description = "Similar to 2: GUARD TOMBS, but inside the coffin is a clay statue of a thin and sly-looking snake-man scholar. Its scrolls have crumbled to dust. The statue contains the same amulet, snake skeleton, and poison as the others.",
)

room_4 = build.Room(
    name = "4: SORCERER TOMB",
    description = "Similar to 2: GUARD TOMBS, but inside the coffin there is a clay statue of a robed snake-man sorcerer wearing a silver ring. If the PCs didn’t already learn that the other statues were hollow, they’ll almost certainly try to pry the ring off, breaking the statue open and revealing the poison gas and amulet. The ring is a magical, but also cursed. If worn on a finger, the fingernail becomes long, bifurcated, and pointed like twin fangs. It can be used like a poison dagger (living targets must Save vs. Poison or take +1d6 poison damage on a hit), but each morning, the wearer must Save vs. Poison or take d6 damage. If they take 6 damage at once from the poison ring, their finger falls off and turns into a snake.",
)

room_5 = build.Room(
    name = "5: DOOR/HAMMER TRAP",
    description = "Blah blah ",
)

# After creating all the rooms, then you say how they are linked up:
room_1.accessible_rooms = [room_2, room_3, room_4, room_5,]
room_2.accessible_rooms = [room_1,]
room_3.accessible_rooms = [room_1,]
room_4.accessible_rooms = [room_1,]
room_5.accessible_rooms = [room_1, "To do:room_6",]

# We craft the items in this coordinate:
room_1_sword = craft.Item(
    name = "Sword",
    description = "A rusty iron sword.",
    damage_die = 4,
    armor_bonus = 0,
    effect = "No effect",
)

# Then place those items in the respective rooms:
room_1.contents = [room_1_sword,]

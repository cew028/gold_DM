import os

import characters
import draw
import prompt

import Locations.coord_0_0 as coord_0_0

def cls():
    """Clear the console."""
    os.system("cls" if os.name == "nt" else "clear")

def main():
    draw.picture(file="Pictures/Logo.txt")
    # you = characters.Player()
    # you.create()
    # draw.picture(file="Pictures/Castle.txt")
    # prompt.open_response("Hi how are you?", ["Good", "Okay", "Bad"])
    coord_0_0.room_1.go_to("2: GUARD TOMBS")
    coord_0_0.room_1.go_to("poop poop")
    
if __name__ == "__main__":
    cls()
    main()
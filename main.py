import os

import draw
import engine

def cls():
    """Clear the console."""
    os.system("cls" if os.name == "nt" else "clear")

def main():
    draw.picture(file="Pictures/Logo.txt")
    # you = characters.Player()
    # you.create()
    # draw.picture(file="Pictures/Castle.txt")
    # prompt.open_response("Hi how are you?", ["Good", "Okay", "Bad"])
    engine.gameplay_loop()
    
if __name__ == "__main__":
    cls()
    main()
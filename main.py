import os

import draw
import engine

def cls():
    """Clear the console."""
    os.system("cls" if os.name == "nt" else "clear")

def main():
    draw.picture(file="Pictures/Logo.txt")
    # engine.you.create()
    # draw.picture(file="Pictures/Castle.txt")
    engine.gameplay_loop()
    
if __name__ == "__main__":
    cls()
    main()
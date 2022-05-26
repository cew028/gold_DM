import characters
import draw
import prompt

def main():
    # you = characters.Player()
    # you.create()
    # draw.picture(100, file="Pictures/Castle.txt")
    prompt.open_response("Hi how are you?", ["Good", "Okay", "Bad"])
    
if __name__ == "__main__":
    main()
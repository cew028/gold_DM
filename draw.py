def frame(width: int = 100, contents: list = []):
    """This function takes as an input a width (default 100) and a list of strings to write.
    It then draws a frame around the written strings (with line breaks after each string).
    It has built-in line breaks for lines longer than the width inputted."""
    print("\n╔", end="")
    for i in range(width-2):
        print("═", end="")
    print("╗")
    for content in contents:
        white_space = width-len(content)-2-1 # The 2 is for the left and right edges of the frame, the 1 is for the leading white space before {content}.
        if white_space > 0:
            # This line fits inside of the frame.
            print(f"║ {content}" + white_space*" " + "║")
        else:
            # This line doesn't fit.
            line = ""
            list_of_words = content.split(" ") # This takes the {content} and produces a list of strings of the words.
            while len(list_of_words) > 0:
                line += list_of_words[0] + " "
                list_of_words.pop(0)
                if len(list_of_words) != 0:
                    if len(line)+len(list_of_words[0]) > width-2-2: # The first 2 is for the frame and the second 2 is for the white space.
                        # If adding the next word makes the line too long.
                        white_space_line = width-len(line)-2-1
                        print(f"║ {line}" + white_space_line*" " + "║")
                        line = ""
                else:
                    white_space_line = width-len(line)-2-1
                    print(f"║ {line}" + white_space_line*" " + "║")
                    line = ""
    print("╚", end="")
    for i in range(width-2):
        print("═", end="")
    print("╝")
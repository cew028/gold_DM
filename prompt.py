class OutsideOptionScopeError(Exception):
    """Raised if you try to answer a question with something that does not answer it."""
    pass

def multiple_choice(question: str = "", options: list = []) -> str:
    """This function takes as input a question and a list of answers (strings).
    It outputs the answer selected."""
    options_letters = []
    for i in range(0,len(options)):
        options_letters.append(chr(ord('@')+i+1))
    print(f"\n{question}")
    for i in range(0,len(options)):
        print(f"[{options_letters[i]}] {options[i]}")
    while True:
        try:
            answer = str(input(">"))
            if answer.capitalize() not in options_letters:
                raise OutsideOptionScopeError
        except (ValueError, OutsideOptionScopeError):
            print("\nThat is not a valid choice.")
            print("Please select one of the given options.")
            continue
        else:
            final_answer = options[ord(answer.capitalize())-1-ord('@')] # This is the term in the list you selected.
            break
    return final_answer

def open_response(question: str = "", options: list =[]) -> str:
    """This function takes as input a question and a list of answers (strings).
    It doesn't show the player the answers.
    When the player types an answer, it checks if what they typed appears in the list of options.
    If it does, it outputs the chosen option."""
    print(f"\n{question}")
    while True:
        try:
            answer = str(input(">"))
            if answer.casefold() not in (option.casefold() for option in options):
                raise OutsideOptionScopeError
        except (ValueError, OutsideOptionScopeError):
            print("\nI don't understand.")
            print("Please try again.")
            continue
        else:
            selected_index = [option.lower() for option in options].index(answer.lower())
            final_answer = options[selected_index]
            break
    return final_answer
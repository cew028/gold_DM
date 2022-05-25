class OutsideOptionScopeError(Exception):
    """Raised if you try to answer a question with something that does not answer it."""
    pass

def multiple_choice(question: str = "", options: list = []) -> int:
    """This function takes as input a question and a list of answers.
    It outputs the answer selected (starting at 0)."""
    options_letters = []
    for i in range(0,len(options)):
        options_letters.append(chr(ord('@')+i+1))
    print(f"\n{question}")
    for i in range(0,len(options)):
        print(f"[{options_letters[i]}] {options[i]}")
    while True:
        try:
            answer = str(input())
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
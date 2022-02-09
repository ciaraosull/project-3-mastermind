# Write your code to expect a terminal of 80 characters wide and 24 rows high



def welcome_note():
    """
    Welcome note and get name input from the user.
    """
    print("**********************")
    print("      Mastermind")
    print("Crack the Code to Win!")
    print("**********************\n")

    name_data = input("Enter your name here to begin: ")
    validate_data(name_data)
    
    print(f"\nWelcome {name_data}")
    print("Have you got what it takes to break the code!\n")

def validate_data(name):
    """
    Validates user input for name
    """
    try:
        if name == "":
            raise ValueError("Please input some type of name")
    except ValueError as e:
        print(f"Try again.  {e}")


welcome_note()


def game_choice():
    """
    Give choice to user to display rules.
    They could be a returning player.
    """
    rules_choice = input("For Game Rules enter R otherwise enter P to Play: ").lower()
    
    if rules_choice == "r":
        print("How to Play....")
        print("Let's Begin!")

    elif rules_choice == "p":
        print("Let's Begin!")

    else:
        print("Sorry, not a valid response\n")
        game_choice()


game_choice()

def start_game():
    guess = input("Please Enter your guess: ")


start_game()



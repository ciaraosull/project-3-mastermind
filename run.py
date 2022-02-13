# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def get_name():
    """
    Welcome note and get name input from the user.
    """
    print("**********************")
    print("      Mastermind")
    print("Crack the Code to Win!")
    print("**********************\n")

    while True:
        name_data = input("Enter your name here to begin:\n")

        if validate_data(name_data):
            print(f"\nWelcome {name_data}")
            print("Have you got what it takes to break the code!\n")
            break


def validate_data(name):
    """
    Validates user input for name
    """
    try:
        if name == "":
            raise ValueError("Please input some type of name\n")

    except ValueError as error:
        print(f"Try again.  {error}")
        return False

    return True


get_name()


def game_choice():
    """
    Give choice to user to display rules.
    They could be a returning player.
    """
    rules_choice = input(
        "For Game Rules enter R otherwise enter P to Play:\n").lower()

    if rules_choice == "r":
        print("How to Play....")
        print("Let's Begin!")

    elif rules_choice == "p":
        print("Let's Begin!")

    else:
        print("Sorry, not a valid response\n")
        game_choice()


game_choice()

# generate random code here?
# calculate how many attemps left.  If over 10 then Game over
# if attemps under 10 then request user guess in start_game function


def start_game():
    """
    Start game to calculate the random code
    """
    guess = input("Please Enter your guess:\n")

    # validate guess


start_game()

# calculate if guess is correct. If it is go to winner message
# if not correct take away an attempt
# calculate code hint
# back to start game for user next guess

# winner message. go to play again or quit goodbye message
# game lost message. got to play again or goodby message

# winner message trigger if code guess is correct
# game lost message. trigger if attemps are over
# play again to back to start get_name
# quit then show goodbye message

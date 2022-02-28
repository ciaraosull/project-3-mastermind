""" Player Class imports """
# import colorama for adding colour
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)


class Player:
    """
    Creates player object and gives it the ability to
    take the user's name, give the choice to the user
    if they want rules displayed,
    take the user's guesses and validate
    all the user's input
    """
    # def __init__(self):
    # pass

    def get_name(self):
        """
        Get name input from the user.
        """
        while True:
            name_data = input("Enter your name here to begin:\n")
            # pass the name through the validate_data method to check
            if self.validate_data(name_data):
                print("\nWelcome " + Fore.GREEN + f"{name_data}")
                print("Have you got what it takes to break the code!\n")
                break

    @staticmethod
    def validate_data(name):
        """
        Validates user input for name
        """
        # If nothing entered eg. only spacebar pressed
        # or just enter hit then return error,
        # otherwise accept all characters for name / nickname
        try:
            if len(name.strip()) == 0:
                # if name == "":
                raise ValueError("Please input some type of name\n")

        except ValueError as error:
            print(Fore.RED + f"Try again.  {error}")
            return False

        return True

    def game_choice(self):
        """
        Give choice to user to display rules.
        They could be a returning player.
        """
        rules_choice = input(
            "For Game Rules enter " +
            Fore.YELLOW + "R " +
            Fore.RESET + "otherwise enter " +
            Fore.GREEN + "P " +
            Fore.RESET + "to Play:\n").lower()

        if rules_choice == "r":
            print(f"{Fore.BLUE}How to Play:\n")

            print(
                f"You have {Fore.YELLOW}10 {Fore.RESET}attempts " +
                "to guess the secret code")

            print("The secret code is 4 numbers between 1-10")
            print("Numbers may be repeated within the secret code!\n")
            print(f"{Fore.YELLOW}Please separate your 4 numbers by a space")
            print("For example: 1 2 3 4\n")
            print(f"{Fore.BLUE}Code Hints:\n")
            print(
                Back.GREEN + "GREEN" +
                Back.RESET + " = correct number in correct position\n")
            print(
                Back.YELLOW + "ORANGE" +
                Back.RESET + " = correct number in wrong position\n")
            print("Code Hint colours are not in order!\n")
            print(f"{Fore.MAGENTA}Let's Begin!\n")

        elif rules_choice == "p":
            print(f"{Fore.MAGENTA}Let's Begin!\n")

        else:
            print(f"{Fore.RED}Sorry, not a valid response\n")
            self.game_choice()

    def start_game(self):
        """
        Start game for user guess to accept numbers separated by 1 space only
        """
        while True:
            try:
                # Iterates through user input and converts to integers.
                # Also strips off white spaces at begining
                # and end if user enters by mistake
                guess = list(
                    map(int, input(
                        "Please Enter your guess:\n").strip(" ").split(' ')))

            except ValueError:
                print(
                    f"{Fore.RED}" +
                    "Please enter 4 numbers separated by one space only\n")
                continue

            if self.validate_guess_input(guess):
                print(f"\nYou Guessed {guess}")
                break

        return guess

    @staticmethod
    def validate_guess_input(values):
        """
        Validates the users input guess to be only 4 numbers and between 1-10
        """
        try:
            if len(values) != 4:
                raise ValueError(
                    "Exactly 4 numbers only, separated by a space.\n" +
                    f"You provided {len(values)} number/s"
                )
        except ValueError as error:
            print(f"{Fore.RED}{error}, please try again.\n")
            return False

        try:
            for i in values:
                if i >= 11 or i <= 0:
                    raise ValueError(
                        "Only guess numbers between 1 - 10."
                        )
        except ValueError as error:
            print(f"{Fore.RED}{error} Please try again.\n")
            return False

        return True

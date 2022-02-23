""" Mastermind Game imports """
# import random for generating random numbers for secret
import random

# import os to help clear terminal for user on replay
import os

# import pyfiglet module for ascii art
import pyfiglet

# import colorama for adding colour
import colorama
from colorama import Fore, Back
colorama.init(autoreset=True)


class Player:
    """ Initialises instance """
    def __init__(self):
        pass

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

    def validate_data(self, name):
        """
        Validates user input for name
        """
        # If nothing entered then return error,
        # otherwise accept all characters for name / nickname
        try:
            if name == "":
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

    def validate_guess_input(self, values):
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


class CodeGenerator:
    """
    Initialises instance
    """
    def __init__(self):
        pass

    def random_code(self, max_range):
        """
        Generate random secret code here
        """
        random_nums = []
        # using list comprehension + randint()
        # to generate random number list
        for i in range(4):
            random_nums.append(random.randint(1, max_range))
        return random_nums

    def match_position(self, secret_code, user_guess):
        """
        Finds the position of the matched numbers
        """
        for nums in range(0, 4):
            if secret_code[nums] == user_guess:
                return nums

    def calculate_code_hint(self, secret_code, user_guess):
        """
        Compare user guess againts secret code and provide hints
        """
        code_hint_green = []
        code_hint_orange = []
        # Variables to put back in a list to
        # check against agin on next guess
        guess = list(user_guess)
        code = list(secret_code)

        if guess == code:
            win_msg = pyfiglet.figlet_format(
                "Winner!", font="standard")
            print(win_msg)
            play_again()

        else:
            for i in range(0, 4):
                if guess[i] == code[i]:
                    code[i] = "-"
                    guess[i] = ""
                    code_hint_green.append(f"{Fore.GREEN}GREEN{Fore.RESET}")

            for i in range(0, 4):
                if guess[i] in code:
                    matched_position = self.match_position(code, guess[i])
                    code[matched_position] = '-'
                    guess[i] = ""
                    code_hint_orange.append(f"{Fore.YELLOW}ORANGE{Fore.RESET}")

        # Iterate through each item and
        # join both lists for printing colour with colorama
        code_hint = (
            ' '.join(str(item) for item in code_hint_green)) + (" ") + (
                ' '.join(str(item) for item in code_hint_orange))

        # to ensure no blank code hint printed for positive UX
        if not code_hint_green and not code_hint_orange:
            print(
                f"Code Hint: {Fore.RED}" +
                "None of those numbers are in the secret code\n")
        else:
            print(f"Code Hint: {code_hint}\n")


def clear():
    """
    Clear screen for user on replay
    """
    os.system("clear")


def play_again():
    """
    Give user choice to play again or quit
    """
    play_choice = input(
            f"{Fore.YELLOW}" +
            f"Play Again? Y or N:{Fore.RESET}\n").lower()
    if play_choice == "y":
        clear()
        print(
            f"{Fore.GREEN}" +
            "You chose Yes! Let's Play!")
        main()

    elif play_choice == "n":
        print(f"{Fore.MAGENTA}Sorry to see you go :-(\n")
        print("Hope you come back soon to play again!")
        exit()

    else:
        print(f"{Fore.RED}Sorry, not a valid response\n")
        play_again()


def welcome():
    """
    Title & welcome message
    """
    title = pyfiglet.figlet_format(
        "Mastermind", font="standard", justify="center")
    print(title)

    subtitle = pyfiglet.figlet_format(
        "Crack The Code", font="digital", justify="center")
    print(subtitle)

    print(Fore.YELLOW + "Created by Ciara O'Sullivan".center(80) + "\n")


def main():
    """
    Run all program functions and methods
    """
    welcome()
    # create objects of the classes to invoke constructors
    player = Player()
    coder = CodeGenerator()
    # calling the instance methods using the object player
    player.get_name()
    player.game_choice()
    # assigning variable secret_code to the method
    # that generates random numbers and pass through max range of 10
    secret_code = coder.random_code(10)

    # for testing only take away print at end
    print(f"The secret code is {secret_code}")

    # Handle guess count for order of running
    guess_left = 10

    while guess_left <= 10:
        if guess_left == 0:
            print(f"{Fore.RED}Sorry, No Guesses Left!\n")
            print(f"The Secret Code was {secret_code}\n")
            lost_msg = pyfiglet.figlet_format(
                "Code Not Cracked", font="digital")
            print(lost_msg)
            play_again()
        else:
            print(
                f"You have {Fore.RED}{guess_left}{Fore.RESET} guesses left\n")
            guess_left -= 1
            # assigning variable user_guess to the method
            # that asks user for their guess
            user_guess = player.start_game()
            # calling the instance methods using the object coder
            coder.calculate_code_hint(secret_code, user_guess)
            coder.match_position(secret_code, user_guess)


if __name__ == "__main__":
    main()

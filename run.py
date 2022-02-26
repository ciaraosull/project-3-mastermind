""" Mastermind Game imports """
# import player class
from player import Player

# import CodeGenerator class
from coder import CodeGenerator

# import os to help clear terminal for user on replay
import os

# import pyfiglet module for ascii art
import pyfiglet

# import colorama for adding colour
import colorama
from colorama import Fore
colorama.init(autoreset=True)


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

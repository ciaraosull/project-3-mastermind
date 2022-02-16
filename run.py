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


def game_choice():
    """
    Give choice to user to display rules.
    They could be a returning player.
    """
    rules_choice = input(
        "For Game Rules enter R otherwise enter P to Play:\n").lower()

    if rules_choice == "r":
        print("How to Play:\n")
        print("You have 10 attemps to guess the secrect code")
        print("The secret code is 4 numbers between 1-10")
        print("Numbers may be repeated within the secret code!\n")
        print("Code Hints:")
        print("* = correct number in correct position")
        print("& = correct number in wrong position")
        print("Code Hint symbols are not in order!")
        print("Let's Begin!\n")

    elif rules_choice == "p":
        print("Let's Begin!\n")

    else:
        print("Sorry, not a valid response\n")
        game_choice()


def random_code(max_range):
    """
    Generate random secret code here
    """
    random_nums = []
    for i in range(4):
        random_nums.append(random.randint(1, max_range))
    return random_nums


def start_game():
    """
    Start game for user guess
    """
    guess = list(map(int, input("Please Enter your guess:\n").split(' ')))
    print(f"You guessed {guess}")
    return guess

    # validate guess entry here


def find_position(secret_code, user_guess):
    """
    Finds the position of the matched numbers
    """
    for i in range(0, 4):
        if secret_code[i] == user_guess:
            return i


def calculate_guess(secret_code, user_guess):
    """
    Compare user guess againts secret code and provide hints
    Handle Guess count
    """
    code_hint = []
    # puts user guess and secret code 
    # back in a list to check against again
    guess = list(user_guess)
    code = list(secret_code)

    if guess == code:
        print("WINNER\n")
        print("Play Again?\n")
        main()
        # play_again option to go here
    else:
        for i in range(0, 4):
            if guess[i] == code[i]:
                code[i] = "-"
                guess[i] = ""
                code_hint.append("*")

        for i in range(0, 4):
            if guess[i] in code:
                matched_position = find_position(code, guess[i])
                code[matched_position] = '-'
                guess[i] = ""
                code_hint.append("&")
    print(f"Code Hint: {code_hint}")


def main():
    """
    Run all program function
    """
    get_name()
    game_choice()
    secret_code = random_code(10)
    # for testing only take away print at end
    print(f"The secret code is {secret_code}")
    guess_left = 10

    while guess_left <= 10:
        if guess_left == 0:
            print("Sorry, No Guesses Left!")
            print(f"The Secret Code was {secret_code}")
            break
            # put play_again() function here
        else:
            print(f"You have {guess_left} guesses left")
            guess_left -= 1
            user_guess = start_game()
            calculate_guess(secret_code, user_guess)
            find_position(secret_code, user_guess)


main()


# winner message. go to play again or quit goodbye message
# game lost message. got to play again or goodby message
# winner message trigger if code guess is correct
# game lost message. trigger if attemps are over
# play again to back to start get_name
# quit then show goodbye message

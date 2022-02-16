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
        print("How to Play....")
        print("Let's Begin!")

    elif rules_choice == "p":
        print("Let's Begin!")

    else:
        print("Sorry, not a valid response\n")
        game_choice()


def random_code(max_range):
    """
    generate random code here
    """
    random_nums = []
    for i in range(4):
        random_nums.append(random.randint(1, max_range))
    return random_nums


# calculate how many attemps left.  If over 10 then Game over
# if attemps under 10 then request user guess in start_game function

def start_game():
    """
    Start game for user guess
    """
    #print("Your guess should contain 4 numbers between 1-9 sepatated by a space.\n")
    guess = list(map(int, input("Please Enter your guess:\n").split(' ')))
    print(f"You guessed {guess}")
    return guess

    # validate guess here


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

            code_hint = []
            guess = list(user_guess)
            code = list(secret_code)

            if guess == code:
                print("winner")
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
                print(f"The Code Hint is {code_hint}")
                start_game()

    #if user_guess == secret_code:
    #   print("winner")
    # elif
    # else:
     #   print("Looser")
    #return


def main():
    """
    Run all program function
    """
    get_name()
    game_choice()
    secret_code = random_code(100)
    # for testing only take away print at end
    print(f"The secret code is {secret_code}")
    user_guess = start_game()
    calculate_guess(secret_code, user_guess)
    find_position(secret_code, user_guess)

main()

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

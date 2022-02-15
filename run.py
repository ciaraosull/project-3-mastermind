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
    generate random code here?
    """
    random_nums = []
    for i in range(4):
        random_nums.append(random.randint(1, max_range))
    # for testing only to delete at end
    print(f"The secret code is {random_nums}")
    return random_nums


# calculate how many attemps left.  If over 10 then Game over
# if attemps under 10 then request user guess in start_game function

def start_game():
    """
    Start game to calculate the random code
    """
    print("Your guess should contain 4 numbers between 1-9 sepatated by a space.\n")
    guess = list(map(int, input("Please Enter your guess:\n").split(' ')))
    print(f"You guessed {guess}")
    return guess

    # validate guess here

def calculate_guess(user_guess, secret_code):
    """
    Compare user guess againts secret code and provides hints
    """
    code_hint = []

    if user_guess == secret_code:
        print("winner")
    else:
        for i in range(0, 4):
            if user_guess[i]  == secret_code[i]:
                secret_code[i] = "-"
                user_guess[i] = ""
                code_hint.append("*")

        for i in range(0, 4):
            if user_guess == secret_code[i]:
                    return i
            matched_position = i
            if user_guess[i] in secret_code:
                secret_code[matched_position] = '-'
                user_guess[i] = ""
                code_hint.append("&")
        print(f"The Code Hint is {code_hint}")


    #if user_guess == secret_code:
     #   print("winner")
    #elif
    #else:
     #   print("Looser")
    #return


def main():
    """
    Run all program function
    """
    get_name()
    game_choice()
    secret_code = random_code(100)
    user_guess = start_game()
    calculate_guess(user_guess, secret_code)

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

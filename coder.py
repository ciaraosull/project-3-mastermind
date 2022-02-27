""" CodeGenerator Class imports """
# import random for generating random numbers for secret
import random

# import colorama for adding colour
import colorama
from colorama import Fore
colorama.init(autoreset=True)


class CodeGenerator:
    """
    Creates coder object and gives it the ability to
    generate the random secret code, finds the matches
    in the user's guess and the secret code and generates
    the code hint for the user
    """
    # def __init__(self):
    #    pass

    def random_code(self, max_range):
        """
        Generate random secret code here
        """
        random_nums = []
        # using list comprehension + randint()
        # to generate random number list
        for nums in range(4):
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
        # check against again on next guess
        guess = list(user_guess)
        code = list(secret_code)

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

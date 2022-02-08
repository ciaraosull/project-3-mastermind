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
    print(f"\nWelcome {name_data}")
    print("Have you got what it takes to break the code!\n")

welcome_note()

def game_choice():
    rules_choice = input("For Game Rules enter R otherwise enter P to Play: ")
    
    if rules_choice == "R":
        print("How to Play....")

    elif rules_choice == "P":
        print("Let's Begin!")

    else:
        print("Sorry, not a valid response\n")
        game_choice()

game_choice()





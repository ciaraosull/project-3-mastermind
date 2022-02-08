# Write your code to expect a terminal of 80 characters wide and 24 rows high

def welcome_note():
    """
    Welcome note and get name input from the user.
    """
    print("Mastermind")
    print("Crack the Code to Win!\n")

    name_str = input("Enter your name here to begin: ")
    print(f"\nWelcome {name_str}")
    print("Have you got what it takes to break the code?")


welcome_note()

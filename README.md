# **Mastermind**

Mastermind - Code-Breaker, is a Python terminal game that runs on Heroku.

View the live project [Here](https://mastermind-code-breaker.herokuapp.com)

This game is based on the board game of [Mastermind]( https://en.wikipedia.org/wiki/Mastermind_(board_game)) from the 1970’s, which is actually based on an even older paper and pencil game called Bulls & Cows.

This game was chosen as it seems it would appeal to the target audience of adults seeking to play an online strategy game for a fun challenge and cognitive stimulation.

According to [Barrow Neurological Institute](https://www.barrowneuro.org/centers-programs/neurorehabilitation/resources/neuro-rehabilitation-apps-and-games/) The Mastermind board game can be used for planning, problem solving, and decision making.  Also, according to [Strom & Barolo (2011)](https://www.researchgate.net/publication/49785492_Using_the_Game_of_Mastermind_to_Teach_Practice_and_Discuss_Scientific_Reasoning_Skills) the Mastermind board game has been adapted for applications in fields such as Maths, Computing and Psychology and used as a tool for teaching logic.  They argue that it can also be utilised to teach topics relevant to the Life Sciences such as experimental design, hypothesis testing, interpreting results and use of controls.

## How To Play

In this game Mastermind – Code Breaker users play to crack the secret code randomly chosen by the computer.  Users are given hints generated by the computer after every attempt to try to logically deduce what the correct secret code is.  

*   The secret code is 4 numbers between 1 - 10 and any of these numbers may be repeated.

* The player has 10 attempts to guess the sceret code.  The correct guess must be all 4 correct numbers in the correct order.

* After every attempt (unless successful) the player is given a code hint.  Every GREEN represents how many numbers were correct and in the correct position.  Every ORANGE represents how many numbers were correct but in the incorrect position.  

* The order of the code hint will be any GREENs first and then ORANGE so it does not match the order of the players numbers in their guess.

    *   For example:

    *   the secret code is 1, 2, 3, 4
    *   the guess is: 1, 3, 5, 4
    *   the code hint will be: GREEN GREEN ORANGE

    *   This represent 1 & 4 as two GREENs and 3 as ORANGE

* If none of the 4 numbers are correct, the player will recieve feedback to state this, otherwise they will not be told which numbers are incorrect.




## User Experience (UX)

### User Stories
A user wants to:


### User Experience Research

### User Experience in this Game
This game takes these key reseach pieces and the users stories mentioned above into consideration to create a positive UX.  The users experience is discussed in more detail below with examples in the Design & Features Sections.

## Features


### Features Left to Implement


### Data Model

**UML - Use Case Diagram**

Unified Modelling Language (UML) was used to visualize the various features of the game. 

* A Use Case Diagram was drafted to capture the games functionaity and relationships with the user.

* The Matermind Game is the system represented by the rectangle below.  The external object is the Primary Actor.  In this game it will be the Player that initiates the use of the system.

* The Use Case in the diagram below are represented in circles and these are the actions that will initiate different tasks within the game.

* The relationship the Player has with the system is represented with a solid line.  The two other relationships are include relationships (executed each time) and extend relationships (executed sometimes), which are represented by a dashed line.

![Use Case Diagram](assets/images/use-case-diagram.png)

**Classes**

Throughout this project, I have opted to use Object Oriented Programming. From the Use Case Diagram the Classes were created.  The game consists of two classes, the Player & the CodeGenerator.  Both of these classes have asscociated methods.  The class diagram below was used to decide what each class does and then design the methods each class should have.

The classes and their asscociated methods are stored in separate files to allow for separating the code into parts that hold related data and functionality.  This will allow any future expansion and development of this project to have a clear structure and also for any code re-use and sharing as well as maintenance.

![Class Diagram](assets/images/class-diagram.png)

**Flow Control**

To design the order in which individual statements, instructions or function calls were executed or evaluated a flow chart was used for the control flow.  Here, the flow of the game was laid out and structured to aid in the design of the control flow statements such as if-elif-else statements, while loops and for loops.  This also allowed the design of the user input validation checks to be visually clear before the code was written.

![Flowchart](assets/images/flowchart.png)


### Design

**Fonts**
[Pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/#:~:text=pyfiglet%20takes%20ASCII%20text%20and,pyfiglet%20module%20%3A%20pip%20install%20pyfiglet) was installed and import pyfiglet was used to generate ascii art for the game.  Pyfiglet was added to requirements.txt then for deployment to Heroku.

The ascii art was chosen for readability for the user from [Figlet.org](http://www.figlet.org/)

**Fonts used were:**

*   Standard Font - for clarity & Line Spacing.  Used on Title & Winner Message

*   Digital Font - for letters having a locked-in effect.  Used on sub-title and game lost message to depict code not broken or code not cracked.  This is a little hard to read but the fun point of using this font is exactly that.  The letters are presented locked in a grid and to read them is on par with trying to figure out and break a code, which fits nicely with the theme of the game.  The text in this font is not detrimental to understanding the game or instructions, it is purely for fun and decoration so it should not matter if it is not read.

**Colour**
To change the font colour and background colour of some words [Colorama](https://pypi.org/project/colorama/) was imported.  Colorama was added to requirements.txt then for deployment.  

A mix of yellow, green, blue and red was used to keep the game play interesting and as a visual que to user for certain feedback.

## Libraries & Technology Used

**Built in Python Libraries**

*   os

The os library was imported to create a function to utilise the os.system to clear the terminal.  This supports a positive user experience on game replay by clearing the previous game play and making the screen clearer and more structured.

*   random

The random library was imported to access the built in method of generating a random number selection using the ranint() method.  This then is used to generate a random sequence of 4 numbers from a range of 1 – 10 for the secret code the user has to crack.

**Other**
* [Colorama](https://pypi.org/project/colorama/) for adding colour to fonts.

*   [Pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/#:~:text=pyfiglet%20takes%20ASCII%20text%20and,pyfiglet%20module%20%3A%20pip%20install%20pyfiglet) for adding ascii art.

*   [LucidCharts](https://www.lucidchart.com/) was used to create the UML Case Diagram, Class Diagram and the Flowchart.

*   Microsoft Photos to edit, crop and save images of charts and diagrams

## Testing

### Interesting Issues & Bugs Found

### Validator Testing

## Deployment

## Credits

## Acknowledgements


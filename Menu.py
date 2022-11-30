from Data import Dialogue
from Data import Basics
# Instantiates the classes
DialogueClass = Dialogue()
Stats = Basics()

"""
TO-DO LIST: 

2. Fix Main Menu Looping Issues
4. Implement Guessing Game
5. Implement Grade Calculator
6. Implement Person Class and Small Program Surrounding It. 
7. Double Check Requirements Before Submission. 

"""


def Hello():
    # Greets the User
    print("Hello there! Welcome to my Review Program.")
    # Asks the user their name and edits the global name variable
    Name = input("Before we begin, what is your name?: ")
    Stats.SetName(Name)
    print("Hello " f"{Stats.GetName()}. I hope you enjoying using my program!")
    print(Basics.Border)
    MainMenu()


def VerifyMainMenuChoice(Choice):  # Exception Handling for Main Menu Input
    while Choice > Stats.GetNumberOfModules() or Choice < 0:
        print("Error, Please try inputting a valid response.")
        print(Basics.Border)
        MainMenu()
        break
    if Choice == 1:
        print(Dialogue.OpeningProgramStatements[1])
        print(Basics.Border)
        import Converter
        Converter.AskForData()
    elif Choice == 2:

    elif Choice == 3:

    elif Choice == 4:

    elif Choice == 5:

    elif Choice == 6:

    elif Choice == 7:


def MainMenu():  # Main Menu
    # Prints options for the user.
    Options = DialogueClass.GetMainMenuDialogue()
    for Text in Options:
        print(Text)

    # Asks the user what part of the program they would like to access?
    Choice = int(input("What program would you like to open?: "))
    VerifyMainMenuChoice(Choice)


# Program Starts Here
Hello()

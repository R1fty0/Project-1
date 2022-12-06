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


def VerifyMainMenuChoice(Choice):  # Exception Handling for Main Menu Input
    while Choice == 0:
        print("Invalid entry, please try again.")
        MainMenu()
    if Choice == 1:  # Type Converter
        print(Dialogue.OpeningProgramStatements[0])
        print(Basics.Border)
        import Converter
        Converter.AskForData()
    elif Choice == 2:  # Grade Calculator
        import GradeCalculator
        print(Dialogue.OpeningProgramStatements[1])
        print(Basics.Border)
        GradeCalculator.AskForParameters()
    elif Choice == 3:  # Lister Program
        import Lister
        print(Dialogue.OpeningProgramStatements[2])
        print(Basics.Border)
        Lister.AskUser()
    elif Choice == 4:  # Guessing Game
        import Game
        print(Dialogue.OpeningProgramStatements[3])
        print(Basics.Border)
        Game.GreetUserAndPresentInstructions()
    elif Choice == 5:  # Tax Calculator
        import TaxCalculator
        print(Dialogue.OpeningProgramStatements[4])
        print(Basics.Border)
        TaxCalculator.AskUserToChooseTypeOfCalculator()
    elif Choice == 6:  # High & Low Calculator
        import LowsAndHighsCalculator
        print(Dialogue.OpeningProgramStatements[5])
        print(Basics.Border)
    elif Choice == 7:  # Person Editor
        import PersonEditor
        print(Dialogue.OpeningProgramStatements[6])
        print(Basics.Border)


def MainMenu():  # Main Menu
    # Prints options for the user.
    Options = DialogueClass.GetMainMenuDialogue()
    for Text in Options:
        print(Text)
    # Asks the user what part of the program they would like to access?
    Choice = int(input("What program would you like to open?: "))
    VerifyMainMenuChoice(Choice)


def Hello():
    # Greets the User
    print("Hello there! Welcome to my Review Program.")
    # Asks the user their name and edits the global name variable
    Name = input("Before we begin, what is your name?: ")
    Stats.SetName(Name)
    print("Hello " f"{Stats.GetName()}. I hope you enjoying using my program!")
    print(Basics.Border)
    MainMenu()


# Program Starts Here
Hello()

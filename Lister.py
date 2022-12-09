from Data import Dialogue
Dialogue = Dialogue()

"""
    Functions below, Imports and Instantiations above.
"""


def AskUser():  # asks user the required values
    StartingNumber = int(input("What is the starting number?: "))
    EndingNumber = int(input("What is the ending number?: "))
    Gap = int(input("What is the gap?: "))
    Calculate(StartingNumber, EndingNumber, Gap)


def Calculate(StartingNumber, EndingNumber, Gap):  # calculates the results
    Factors = range(StartingNumber, EndingNumber, Gap)
    Results = []
    for Number in Factors:
        Results.append(Number)
    PrintResults(Results)


def PrintResults(Results):  # prints the results
    print("The output of the data you inputted is " f"{Results}")  # How to remove the brackets when this is printed?
    ReturnToMainMenu()


def ReturnToMainMenu():  # return to menu or restart program function
    Options = Dialogue.GetReturnToMainMenuDialogue()
    for Text in Options:
        print(Text)
    Choice = int(input("Input your choice: "))

    while Choice > len(Options) or Choice < 0:  # asks user to try again
        print("Please choose a valid option.")
        ReturnToMainMenu()
    if Choice == 1:  # returns user to main menu
        import Menu
        Menu.MainMenu()
    elif Choice == 2:  # restarts module
        print("Restarting Program!")
        AskUser()
    else:  # asks user to try again
        print("Incorrect Input Detected. Please Try Again!")
        ReturnToMainMenu()

from Data import Dialogue
DialogueClass = Dialogue()


def AskUser():
    StartingNumber = int(input("What is the starting number?: "))
    EndingNumber = int(input("What is the ending number?: "))
    Gap = int(input("What is the gap?: "))
    Calculate(StartingNumber, EndingNumber, Gap)


def Calculate(StartingNumber, EndingNumber, Gap):
    Factors = range(StartingNumber, EndingNumber, Gap)
    Results = []
    for Number in Factors:
        Results.append(Number)
    PrintResults(Results)


def PrintResults(Results):
    print("The output of the data you inputted is " f"{Results}")  # How to remove the brackets when this is printed?
    ReturnToMainMenu()


def ReturnToMainMenu():  # Return to Menu or Restart Program Function
    Options = DialogueClass.GetReturnToMainMenuDialogue()
    for Text in Options:
        print(Text)
    Choice = int(input("Input your choice: "))

    while Choice > len(Options) or Choice < 0:
        print("Please choose a valid option.")
        ReturnToMainMenu()
    if Choice == 1:
        import Menu
        Menu.MainMenu()
    elif Choice == 2:
        print("Restarting Program!")
        AskUser()
    else:
        print("Incorrect Input Detected. Please Try Again!")
        ReturnToMainMenu()


AskUser()

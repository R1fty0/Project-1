from Data import Basics
from Data import Dialogue
Dialogue = Dialogue()
Values = []
NumberOfValues = 0

"""
    Imports and Variables above, functions below.
"""


def ReturnToMainMenu():  # Return to Menu or Restart Program Function
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
        Start()
    else:  # asks user to try again
        print("Incorrect Input Detected. Please Try Again!")
        ReturnToMainMenu()


def PrintValues(Max, Min, Avg):  # prints results
    print(f"The smallest value you entered was {Min}. The largest value you enters was {Max}. "
          f"The average value of all the ones you entered was {Avg}.")
    ReturnToMainMenu()


def Start():  # asks user how many values they would like to enter
    global NumberOfValues
    NumberOfValues = int(input("How many values would you like to enter?: "))
    print(Basics.Border)
    AskForValues()


def AskForValues():  # asks user for values
    CurrentEntry = 0
    while CurrentEntry != NumberOfValues:
        CurrentEntry = CurrentEntry + 1
        Values.append(input("Enter a value: "))
        print(Basics.Border)
    Calculate()


def Calculate():  # calculates values
    MaxValue = max(Values)  # minimum value
    MinValue = min(Values)  # maximum value
    AverageValue = 0

    for Number in Values:  # average value
        AverageValue = AverageValue + float(Number)

    AverageValue = AverageValue/int(len(Values))

    PrintValues(MaxValue, MinValue, AverageValue)

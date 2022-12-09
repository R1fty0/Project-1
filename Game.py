# Imports
from Data import GuessingGameInfo
from Data import Dialogue
from Data import Basics
import random

# Instantiation of classes
GuessingGame = GuessingGameInfo()
Dialogue = Dialogue()

# Variables used during the game
CurrentResult = 1
CurrentQuestion = 1
CurrentHint = 1
CurrentAnswer = 1


"""
    Imports and Variables above, functions down below.
"""


def ReturnToMainMenu():  # return to main menu or restart module
    Options = Dialogue.GetReturnToMainMenuDialogue()
    for Text in Options:
        print(Text)
    Choice = int(input("Input your choice: "))

    # Exception Handling for User's Choice
    while Choice > len(Options) or Choice < 0:  # asks user to try again
        print("Please choose a valid option.")
        ReturnToMainMenu()
    if Choice == 1:  # returns user to main menu
        import Menu
        Menu.MainMenu()
    elif Choice == 2:  # restarts module
        print("Restarting Program!")
        GenerateResult()
    else:  # asks user to try again
        print("Incorrect Input Detected. Please Try Again!")
        ReturnToMainMenu()


def AskAndCheckAnswer():  # asks user what their answer is and checks it
    UserAnswer = input("What is your answer?: ")  # asks user for answer

    # checks answer
    while float(UserAnswer) != float(CurrentAnswer):
        print("Wrong Answer! Take a minute and try again!")
        print(Basics.Border)
        AskAndCheckAnswer()
        break
    else:
        print("Congratulations, you got the right answer! Well Done!")
        print(Basics.Border)
        ReturnToMainMenu()


def PrintHint():  # prints a hint for the user
    print("Your hint is: " f"{CurrentHint}")
    AskAndCheckAnswer()


def VerifyChoice(Choice, NumberOfOptions):  # exception handling for whether the user wants a hint or not
    while Choice > NumberOfOptions:
        print("Invalid Choice, Please Try Again!")
        print(Basics.Border)
        AskUserForHint()
        break
    if Choice == 1:
        print(Basics.Border)
        PrintHint()
    elif Choice == 2:
        print(Basics.Border)
        AskAndCheckAnswer()


def AskUserForHint():
    Options = Dialogue.GuessingGameHintPrompt
    print("Your question is: " f"{CurrentQuestion}")
    for Text in Options:
        print(Text)
    Choice = int(input("What is your choice?: "))
    VerifyChoice(Choice, len(Options))


def GenerateResult():  # generates a random result that is used for the question, hint and answer
    global CurrentResult
    CurrentResult = int(random.randrange(GuessingGameInfo.TotalAmountOfQuestions))

    global CurrentQuestion
    CurrentQuestion = GuessingGameInfo.Question[CurrentResult]

    global CurrentHint
    CurrentHint = GuessingGameInfo.Hint[CurrentResult]

    global CurrentAnswer
    CurrentAnswer = GuessingGameInfo.Answer[CurrentResult]

    AskUserForHint()


def GreetUserAndPresentInstructions():  # what the name says
    # Prints a greeting to the user as well as the instruction of the game.
    Text = Dialogue.GetGuessingGameInstructions()
    for Length in Text:
        print(Length)

    print(Basics.Border)
    GenerateResult()




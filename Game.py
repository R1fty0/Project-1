from Data import GuessingGameInfo
from Data import Dialogue
from Data import Basics
import random

GuessingGame = GuessingGameInfo()
Dialogue = Dialogue()

CurrentResult = 1
CurrentQuestion = 1
CurrentHint = 1
CurrentAnswer = 1


def ReturnToMainMenu():  # Return to Menu or Restart Program Function
    Options = Dialogue.GetReturnToMainMenuDialogue()
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
        GenerateResult()
    else:
        print("Incorrect Input Detected. Please Try Again!")
        ReturnToMainMenu()


def AskAndCheckAnswer():
    UserAnswer = input("What is your answer?: ")

    while float(UserAnswer) != float(CurrentAnswer):
        print("Wrong Answer! Take a minute and try again!")
        print(Basics.Border)
        AskAndCheckAnswer()
        break
    else:
        print("Congratulations, you got the right answer! Well Done!")
        print(Basics.Border)
        ReturnToMainMenu()


def PrintHint():
    print("Your hint is: " f"{CurrentHint}")
    AskAndCheckAnswer()


def VerifyChoice(Choice, NumberOfOptions):
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
    Options = Dialogue.GuessingGameOptions
    print("Your question is: " f"{CurrentQuestion}")
    for Text in Options:
        print(Text)
    Choice = int(input("What is your choice?: "))
    VerifyChoice(Choice, len(Options))


def GenerateResult():
    global CurrentResult
    CurrentResult = int(random.randrange(GuessingGameInfo.AmountOfQuestions))

    global CurrentQuestion
    CurrentQuestion = GuessingGameInfo.Question[CurrentResult]

    global CurrentHint
    CurrentHint = GuessingGameInfo.Hint[CurrentResult]

    global CurrentAnswer
    CurrentAnswer = GuessingGameInfo.Answer[CurrentResult]

    AskUserForHint()


def GreetUserAndPresentInstructions():
    # Prints a greeting to the user as well as the instruction of the game.
    Text = Dialogue.GetGuessingGameInstructions()
    for Length in Text:
        print(Length)

    print(Basics.Border)
    GenerateResult()




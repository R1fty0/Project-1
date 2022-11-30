from Data import GuessingGame
from Data import Dialogue
import random

GuessingGame = GuessingGame()
Dialogue = Dialogue()

Result = 1
Question = 1
Hint = 1
Answer = 1


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

    while float(UserAnswer) != float(Answer):
        print("Wrong Answer! Take a minute and try again!")
        print(Dialogue.Border)
        AskAndCheckAnswer()
        break
    else:
        print("Congratulations, you got the right answer! Well Done!")
        print(Dialogue.Border)
        ReturnToMainMenu()


def PrintHint():
    print("Your hint is: " f"{Hint}")
    AskAndCheckAnswer()


def VerifyChoice(Choice, NumberOfOptions):
    while Choice > NumberOfOptions:
        print("Invalid Choice, Please Try Again!")
        print(Dialogue.Border)
        AskUserForHint()
        break
    if Choice == 1:
        print(Dialogue.Border)
        PrintHint()
    elif Choice == 2:
        print(Dialogue.Border)
        AskAndCheckAnswer()


def AskUserForHint():
    Options = Dialogue.GuessingGameOptions
    print("Your question is: " f"{Question}")
    for Text in Options:
        print(Text)
    Choice = int(input("What is your choice?: "))
    VerifyChoice(Choice, len(Options))


def GenerateResult():
    global Result
    Result = int(random.randrange(GuessingGame.AmountOfQuestions))

    global Question
    Question = GuessingGame.Question[Result]

    global Hint
    Hint = GuessingGame.Hint[Result]

    global Answer
    Answer = GuessingGame.Answer[Result]

    AskUserForHint()


def GreetUserAndPresentInstructions():
    # Prints a greeting to the user as well as the instruction of the game.
    Text = Dialogue.GetGuessingGameInstructions()
    for Length in Text:
        print(Length)

    print(Dialogue.Border)
    GenerateResult()


GreetUserAndPresentInstructions()

from Data import Basics
from Data import Dialogue
Basics = Basics()

AmountOfAssignments = 0
Grades = []


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
        AskForParameters()
    else:
        print("Incorrect Input Detected. Please Try Again!")
        ReturnToMainMenu()


def AskForParameters():
    print(f"Welcome to the Grade Calculator {Basics.GetName()}!")
    global AmountOfAssignments
    AmountOfAssignments = int(input("How many assignments did you complete in the course you took?:"))
    print(Basics.Border)
    InputGrades()


def InputGrades():
    CurrentEntry = 0
    while CurrentEntry != AmountOfAssignments:
        CurrentEntry = CurrentEntry + 1
        Grades.append(input("What is the grade for one of your assignments as a percent?: "))
        print(Basics.Border)
    Calculate()


def Calculate():
    TotalScore = 0
    for X in Grades:
        TotalScore = TotalScore + int(X)
        TotalScore = TotalScore/100
        TotalScore = TotalScore * 100
    PrintResults(TotalScore)


def PrintResults(TotalGrade):
    print(f"Your total grade in the course is {TotalGrade}%. ")
    print(Basics.Border)

    if TotalGrade == 100:
        print("Well Done, You Aced the Course!")
        print(Basics.Border)
    elif TotalGrade >= 100 or TotalGrade <= 0:
        print("Wait a minute...something ain't right!")
        print(Basics.Border)
    elif TotalGrade <= 50 or TotalGrade <= 0:
        print("Ouch, You failed the course! Take your losses and move on with life...")
    elif 86.0 <= TotalGrade < 100:
        print("You got an A in the course, well done!")
    elif 73.0 <= TotalGrade < 86.0:
        print("You got a B in the course, not bad, but needs some improvement!")
    elif 67.0 <= TotalGrade < 73.0:
        print("You got a C+ in the course, Yikes! Looks like you really need to work on some things...")
    elif 73.0 <= TotalGrade < 86.0:
        print("Woah, you got a C in the course...maybe you need to rethink your life choices?")

    ReturnToMainMenu()
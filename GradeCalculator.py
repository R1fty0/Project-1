# check Data class for more info about these two imports
from Data import Basics
from Data import Dialogue

# instantiates the previously imported classes
Dialogue = Dialogue()
Basics = Basics()

AmountOfAssignments = 0
Grades = []

"""
    Imports and Variables above, Functions below.
"""


def ReturnToMainMenu():  # Return to Menu or Restart Program Function
    Options = Dialogue.GetReturnToMainMenuDialogue()
    for Text in Options:
        print(Text)
    Choice = int(input("Input your choice: "))

    while Choice > len(Options) or Choice < 0:  # asks user to try again and input a valid answer
        print("Please choose a valid option.")
        ReturnToMainMenu()
    if Choice == 1:  # returns user back to main menu
        import Menu
        Menu.MainMenu()
    elif Choice == 2:  # restarts this module
        print("Restarting Program!")
        AskForParameters()
    else:  # asks user to try again and input a valid answer if they inputted an answer the program does not recognize
        print("Incorrect Input Detected. Please Try Again!")
        ReturnToMainMenu()


def AskForParameters():  # asks the user how many assignments did they complete in their course
    print(f"Welcome to the Grade Calculator {Basics.GetName()}!")
    global AmountOfAssignments
    AmountOfAssignments = int(input("How many assignments did you complete in the course you took?:"))
    print(Basics.Border)
    InputGrades()


def InputGrades():  # asks user to input grades
    CurrentEntry = 0
    while CurrentEntry != AmountOfAssignments:
        CurrentEntry = CurrentEntry + 1
        Grades.append(input("What was the grade for one of your assignments as a percent? (out of /100): "))
        print(Basics.Border)
    Calculate()


def Calculate():  # calculates grades
    TotalScore = 0
    for X in Grades:  # loops through grades and adds them to the total grade
        TotalScore = TotalScore + int(X)
    if TotalScore > 100:  # if user score is greater than 100, then divide the score by the total amount of assignments
        TotalScore = TotalScore / AmountOfAssignments
    PrintResults(TotalScore)  # prints results


def PrintResults(TotalGrade):  # Prints User Results
    print(f"Your grade in the course is {TotalGrade}%. ")  # prints user's total grade
    print(Basics.Border)

    # Prints a message based on the letter grade tha corresponds with the user's percentages
    if TotalGrade == 100:
        print("Well Done, You Aced the Course!")
        print(Basics.Border)
    elif TotalGrade >= 100 or TotalGrade <= 0:
        print("Wait a minute...something ain't right!")
        print(Basics.Border)
    elif TotalGrade <= 50 or TotalGrade <= 0:
        print("Ouch, You failed the course! Take your losses and move on with life...")
        print(Basics.Border)
    elif 86.0 <= TotalGrade < 100:
        print("You got an A in the course, well done!")
        print(Basics.Border)
    elif 73.0 <= TotalGrade < 86.0:
        print("You got a B in the course, not bad, but needs some improvement!")
        print(Basics.Border)
    elif 67.0 <= TotalGrade < 73.0:
        print("You got a C+ in the course, Yikes! Looks like you really need to work on some things...")
        print(Basics.Border)
    elif 73.0 <= TotalGrade < 86.0:
        print("Woah, you got a C in the course...maybe you need to rethink your life choices?")
        print(Basics.Border)

    ReturnToMainMenu()

from Data import Basics
Values = []
NumberOfValues = 0


def Start():
    global NumberOfValues
    NumberOfValues = int(input("How many values would you like to enter?: "))
    print(Basics.Border)
    AskForValues()


def AskForValues():
    CurrentEntry = 0
    while CurrentEntry != NumberOfValues:
        CurrentEntry = CurrentEntry + 1
        Values.append(input("Enter a value:"))
        print(Basics.Border)


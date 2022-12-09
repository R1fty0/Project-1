from Data import Dialogue
from Data import Basics

Basics = Basics()
DialogueClass = Dialogue()


def Hello():  # Greets User
    print("Welcome to the Type Converter " f"{Basics.GetName()}")
    AskForData()


def ConvertData(Data):  # Asks User for Data and the type that they would like to convert the data to.
    TypeToConvertTo = input("What data type would you like to convert your data to " f"{Basics.GetName()}? Input the full name of the type (Float, String, Integer):")
    print(Basics.Border)

    # Exception Handling for Data Conversion
    if TypeToConvertTo.upper() == "FLOAT" and type(Data) != type(float):  # Converts Data to Float
        Data = float(Data)
        PrintResults(Data, "Float")
    if TypeToConvertTo.upper() == "STRING" and type(Data) != type(str):  # Converts Data to String
        Data = str(Data)
        PrintResults(Data, "String")
    if TypeToConvertTo.upper() == "INTEGER" and type(Data) != type(int):  # Converts Data to integer
        Data = float(Data)
        PrintResults(Data, "Integer")
    else:  # Asks user the same question if the user misspell the word.
        print("Incorrect Input Detected. Please Try Again. "
              "A reminder to please double check your spelling before continuing.")
        print(Basics.Border)
        ConvertData(Data)


def AskForData():  # Asks user for number
    Metric = input("What is the numerical quantity that you are looking to convert " f"{Basics.GetName()}?: ")
    AskForData(Metric)


def ReturnToMainMenu():  # Returns to the Main Menu or Restarts the Program
    Options = DialogueClass.GetReturnToMainMenuDialogue()
    for Text in Options:  # Prints options for user
        print(Text)
    Choice = int(input("Input your choice: "))

    # Exception handling for user choice
    while Choice > len(Options) or Choice < 0:  # asks user to try again if they did not input a valid option
        print("Please choose a valid option.")
        ReturnToMainMenu()
    if Choice == 1:  # returns to main menu
        import Menu
        Menu.MainMenu()
    elif Choice == 2:  # restarts this module
        print("Restarting Program!")
        AskForData()
    else:  # if user inputs something odd, asks them to try again regardless
        print("Incorrect Input Detected. Please Try Again!")
        ReturnToMainMenu()


def PrintResults(Data, DataType):
    # Prints Answer
    print("The data you inputted: " f"{Data} has now been converted to a " f"{DataType}." + f"{type(Data)}")
    ReturnToMainMenu()


AskForData()
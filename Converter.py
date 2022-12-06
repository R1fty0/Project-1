from Data import Dialogue
from Data import Basics

Basics = Basics()
DialogueClass = Dialogue()
Metric = "data"

# NEEDS TO BE DEBUGGED


def ConvertData(Data):
    print("Welcome to the Type Converter " f"{Basics.GetName()}")
    TypeToConvertTo = input("What data type would you like to convert your data to " f"{Basics.GetName()}? Input the full name of the type:")

    # Exception Handling and Data Conversion
    if TypeToConvertTo.upper() == "FLOAT" and type(Data) != type(float):  # Converts Data to Float
        Data = float(Data)
        PrintResults(Data, "Float")
    if TypeToConvertTo.upper() == "STRING" and type(Data) != type(str):  # Converts Data to String
        Data = str(Data)
        PrintResults(Data, "String")
    if TypeToConvertTo.upper() == "INTEGER" and type(Data) != type(int):  # Converts Data to integer
        Data = float(Data)
        PrintResults(Data, "Integer")


def AskForData():
    global Metric
    Metric = input("What is the quantity you are looking to convert " f"{Basics.GetName()}?: ")
    ConvertData(Metric)


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
        AskForData()
    else:
        print("Incorrect Input Detected. Please Try Again!")
        ReturnToMainMenu()


def PrintResults(Data, DataType):
    # Prints Answer
    print("The data you inputted: " f"{Data} has now been converted to a " f"{DataType}." + f"{type(Data)}")
    ReturnToMainMenu()

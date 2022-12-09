
# Class containing Dialogue for the entire program.
class Dialogue:

    MainMenu = ["Welcome to the Main Menu!:", "Press (1) to open the Data Type Converter!",
                "Press (2) to open the Grade Calculator program!", "Press (3) to use the Lister program!",
                "Press (4) to play the Guessing Game!", "Press (5) to  run the Financial Calculator and Manager!",
                "Press (6) to open the Highs and Lows Calculator!", "Press (7) to open the Person editor!"]  # main menu dialogue

    def GetMainMenuDialogue(self):  # getter for main menu dialogue
        return self.MainMenu

    ReturnToMainMenu = ["Press (1) to return to the Main Menu.", "Press (2) if you would to re-use this program again."]  # return to main menu dialogue

    def GetReturnToMainMenuDialogue(self):  # getter for return to main menu dialogue
        return self.ReturnToMainMenu

    GuessingGameInstructions = ["Welcome to the Guessing Game!", "In this game, you will be tasked with guessing the correct number. ",
                                "You will have the option of viewing a hint if you would like.", "Good Luck!"]  # instructions for guessing game

    def GetGuessingGameInstructions(self):  # getter for guessing game instructions dialogue
        return self.GuessingGameInstructions

    GuessingGameHintPrompt = ["To view your hint, Press (1).",
                              "To skip past your hint and answer the question, Press (2)."]  # dialogue for guessing game hint prompt

    def GetGuessingGameOptions(self):  # getter for guessing game hint prompt
        return self.GuessingGameHintPrompt

    OpeningProgramStatements = ["Running the Type Converter...", "Running the Grade Calculator...", "Starting the Lister Program...",
                                "Booting up the Guessing Game...", "Running the Financial Program now...",
                                "Initializing the Scripts for the Highs and Lows Calculator...", "Creating the Environment for the Person Editor to run..."]  # dialogue used during the opening of each module

    TaxCalculatorDialogue = ["Welcome to the Finance Calculator and Manager!", "Press (1) to use the Tax Calculator.", "Press (2) to use the Bank Account Manager."]  # tax calculator options


class Basics:  # Contains variables and other parameters used repetitively throughout the program.
    Name = "Mohit"
    NumberOfModules = 7
    Border = "_________________________________________________________________________________"

    def SetName(self, Name):  # sets user's name
        self.Name = Name

    def GetName(self):  # returns user name
        return self.Name

    def GetNumberOfModules(self):  # returns the number of modules in the program
        return self.NumberOfModules


class GuessingGameInfo:  # class contain lists of info used in the guessing game
    Question = ["How many months are in a year? ", "How many hours are in a day?",
                "What is the average age of retirement?", "How many hours are in a week?",
                " What is the average life expectancy of people in this country"]  # list containing all possible questions

    Hint = ["It is half of the hours in a day", " It is a multiple of 12",
            "It is 37 years younger than the oldest person alive", "It is the length of 7 whole days",
            "We live roughly a year longer than our fellow Americans"]  # list containing all possible hints

    Answer = [12, 24, 65, 168, 81.1]  # list containing all possible answers

    TotalAmountOfQuestions = len(Question)  # total number of questions, hints and answers




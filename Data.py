
# Class containing Dialogue for the entire program.
class Dialogue:

    MainMenu = ["Welcome to the Main Menu!:", "Press (1) to open the Data Type Converter!",
                "Press (2) to open the Grade Calculator program!", "Press (3) to use the Lister program!",
                "Press (4) to play the Guessing Game!", "Press (5) to  run the Financial Calculator and Manager!",
                "Press (6) to open the Highs and Lows Calculator!", "Press (7) to open the Person editor!"]

    def GetMainMenuDialogue(self):  # Returns the text for the options part of the Main Menu.
        return self.MainMenu

    ReturnToMainMenu = ["Press (1) to return to the Main Menu.", "Press (2) if you would to re-use this program again."]

    def GetReturnToMainMenuDialogue(self):  # Returns the text for the options part of the Return to Main Menu function.
        return self.ReturnToMainMenu

    TaxCalculatorReturnToMenu = ["Press (1) to Return to the Main Menu.", "Press (2) to restart the program."]

    def GetTaxCalculatorReturnToMenuDialogue(self):
        return self.TaxCalculatorReturnToMenu

    GuessingGameInstructions = ["Welcome to the Guessing Game!", "In this game, you will be tasked with guessing the correct number. ",
                                "You will have the option of viewing a hint if you would like.", "Good Luck!"]

    def GetGuessingGameInstructions(self):
        return self.GuessingGameInstructions

    GuessingGameOptions = ["To view your hint, Press (1).",
                           "To skip past your hint and answer the question, Press (2)."]

    def GetGuessingGameOptions(self):
        return self.GuessingGameOptions

    OpeningProgramStatements = ["Running the Type Converter...", "Running the Grade Calculator...", "Starting the Lister Program...",
                                "Booting up the Guessing Game...", "Running the Financial Program now...",
                                "Initializing the Scripts for the Highs and Lows Calculator...", "Creating the Environment for the Person Editor to run..."]

    TaxCalculatorDialogue = ["Welcome to the Finance Calculator and Manager!", "Press (1) to use the Tax Calculator.", "Press (2) to use the Bank Account Manager."]



class Basics:  # Contains variables and other parameters used repetitively throughout the program.
    Name = "Mohit"
    NumberOfModules = 5
    Border = "_________________________________________________________________________________"

    def SetName(self, Name):
        self.Name = Name

    def GetName(self):
        return self.Name

    def GetNumberOfModules(self):
        return self.NumberOfModules


class GuessingGameInfo:
    Question = ["How many months are in a year? ", "How many hours are in a day?",
                "What is the average age of retirement?", "How many hours are in a week?",
                " What is the average life expectancy of people in this country"]

    Hint = ["It is half of the hours in a day", " It is a multiple of 12",
            "It is 37 years younger than the oldest person alive", "It is the length of 7 whole days",
            "We live roughly a year longer than our fellow Americans"]

    Answer = [12, 24, 65, 168, 81.1]

    AmountOfQuestions = len(Question)




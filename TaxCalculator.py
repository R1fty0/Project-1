from Data import Dialogue
from Data import Basics as Border
DialogueClass = Dialogue()

# May add to Class
UserBankAccountBalance = 0
PriceOfItem = 0
TotalPrice = 0
ItemsThatCanBeBought = 0
ItemTax = 0
ItemCost = 0


def AskUserToChooseTypeOfCalculator():
    for Options in Dialogue.TaxCalculatorDialogue:
        print(Options)
    Choice = int(input("What part of this application would you like to use?: "))
    if Choice == 1:
        print("Proceeding to the Tax Calculator.")
        print(Border.Border)
        AskForTaxCalculatorData()
    elif Choice == 2:
        print("Opening the Bank Account Manager as we speak...")
        print(Border.Border)
        AskForBankAccountData()
    else:
        print("Not a valid option! Please try again!")
        print(Border.Border)
        AskUserToChooseTypeOfCalculator()

def AskForBankAccountData():
    global UserBankAccountBalance
    UserBankAccountBalance = float(input("How much money would you like to deposit into your bank account?: "))
    global PriceOfItem
    PriceOfItem = float(input("What is the price of the item you are looking to purchase?: "))
    print(Border.Border)
    Calculations(2)


def AskForTaxCalculatorData():  # Asks the user the information required to calculate the tax on an item.
    print("Just type in the numerical value as the answer for the following questions.")
    global ItemCost
    ItemCost = float(input("What is the cost of the item?: "))
    global ItemTax
    ItemTax = float(input("How much tax is being applied to the item?: "))
    print(Border.Border)
    Calculations(1)


def Calculations(ProgramType):  # This method completes the tax calculations.
    if ProgramType == 1:
        global ItemTax
        ItemTax = ItemTax / 100
        ItemTax = float(ItemCost * ItemTax)
        price = ItemCost + ItemTax
        global TotalPrice
        TotalPrice = price
        PrintResults(1)
    elif ProgramType == 2:
        AmountOfItems = UserBankAccountBalance // PriceOfItem
        global ItemsThatCanBeBought
        ItemsThatCanBeBought = AmountOfItems
        PrintResults(2)


def ReturnToMainMenu():  # Return to Menu or Restart Program Function
    Options = DialogueClass.GetTaxCalculatorReturnToMenuDialogue()
    for Text in Options:
        print(Text)
    Choice = int(input("Input your choice: "))
    print(Border.Border)

    while Choice > len(Options) or Choice < 0:
        print("Please choose a valid option.")
        print(Border.Border)
        ReturnToMainMenu()
    if Choice == 1:
        import Menu
        print("Returning to the Main Menu.")
        print(Border.Border)
        Menu.MainMenu()
    elif Choice == 2:
        print("Restarting the Program.")
        print(Border.Border)
        AskUserToChooseTypeOfCalculator()
    else:
        print("Incorrect Input Detected. Please Try Again!")
        print(Border.Border)
        ReturnToMainMenu()


def PrintResults(ProgramType):  # Prints the price total with tax included.
    if ProgramType == 1:
        print("The price of the item you have with tax is: " + str(TotalPrice) + " dollars Canadian. ")
        print(Border.Border)
        ReturnToMainMenu()
    elif ProgramType == 2:
        print(f" You can buy {ItemsThatCanBeBought} items " + f" with your current bank balance of {UserBankAccountBalance} dollars Canadian. ")
        print(Border.Border)
        ReturnToMainMenu()

AskUserToChooseTypeOfCalculator()


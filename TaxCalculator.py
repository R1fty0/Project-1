from Data import Dialogue
from Data import Basics as Border
DialogueClass = Dialogue()

# Variables used throughout module
UserBankAccountBalance = 0
PriceOfItem = 0
TotalPrice = 0
ItemsThatCanBeBought = 0
ItemTax = 0
ItemCost = 0


def AskUserToChooseTypeOfCalculator():  # asks user which part of the module they want to use
    for Options in Dialogue.TaxCalculatorDialogue:
        print(Options)
    Choice = int(input("What part of this application would you like to use?: "))

    # exception handling for user choice
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


def AskForBankAccountData():  # asks for parameters needed for the Bank Account manager
    global UserBankAccountBalance
    UserBankAccountBalance = float(input("How much money would you like to deposit into your bank account?: "))  # asks user how much money they want to deposit in their bank account
    global PriceOfItem
    PriceOfItem = float(input("What is the price of the item you are looking to purchase?: "))  # asks user for price of item
    print(Border.Border)
    Calculations(2)


def AskForTaxCalculatorData():  # Asks the user the information required to calculate the tax on an item.
    print("Just type in the numerical value as the answer for the following questions.")
    global ItemCost
    ItemCost = float(input("What is the cost of the item?: "))  # asks user for cost of item
    global ItemTax
    ItemTax = float(input("How much tax is being applied to the item?: "))  # asks user for tax being applied to the item
    print(Border.Border)
    Calculations(1)


def Calculations(ProgramType):  # completes calculations
    if ProgramType == 1:  # completes tax calculator calculations
        global ItemTax
        ItemTax = ItemTax / 100
        ItemTax = float(ItemCost * ItemTax)
        price = ItemCost + ItemTax
        global TotalPrice
        TotalPrice = price
        PrintResults(1)

    elif ProgramType == 2:  # completes bank account manager calculations
        AmountOfItems = UserBankAccountBalance // PriceOfItem
        global ItemsThatCanBeBought
        ItemsThatCanBeBought = AmountOfItems
        PrintResults(2)


def ReturnToMainMenu():  # Return to Menu or Restart Program Function
    Options = DialogueClass.ReturnToMainMenu()
    for Text in Options:
        print(Text)
    Choice = int(input("Input your choice: "))
    print(Border.Border)

    while Choice > len(Options) or Choice < 0:  # asks user to try again
        print("Please choose a valid option.")
        print(Border.Border)
        ReturnToMainMenu()
    if Choice == 1:  # returns user to main menu
        import Menu
        print("Returning to the Main Menu.")
        print(Border.Border)
        Menu.MainMenu()
    elif Choice == 2:  # restarts module
        print("Restarting the Program.")
        print(Border.Border)
        AskUserToChooseTypeOfCalculator()
    else:  # asks user to try again
        print("Incorrect Input Detected. Please Try Again!")
        print(Border.Border)
        ReturnToMainMenu()


def PrintResults(ProgramType):  # prints results for both parts of module
    if ProgramType == 1:  # tax calculator result
        print("The price of the item you have with tax is: " + str(TotalPrice) + " dollars Canadian. ")
        print(Border.Border)
        ReturnToMainMenu()
    elif ProgramType == 2:  # bank account manager result
        print(f" You can buy {ItemsThatCanBeBought} items " + f" with your current bank balance of {UserBankAccountBalance} dollars Canadian. ")
        print(Border.Border)
        ReturnToMainMenu()

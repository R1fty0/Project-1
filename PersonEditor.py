# imports
import Menu
from Data import Basics

# Instantiation of Basics class
Basics = Basics()


class Person:  # person class
    def __init__(self, name, age, favoriteQuote, favoriteQuoteAuthor):  # 4 variables required - name, age, favorite quote and the author of that quote
        self.name = name
        self.age = age
        self.favoriteQuote = favoriteQuote
        self.favoriteQuoteAuthor = favoriteQuoteAuthor

    def Name(self, Task):  # returns or sets the variable depending on the task assigned
        if Task == 1:  # Getter
            return self.name
        elif Task == 2:  # Setter
            self.name = input("What would you like to name this person?")

    def GetAge(self):  # returns age variable
        return self.age  # Getter

    def SetAge(self, Age):  # sets the value of the age variable
        self.age = Age  # Setter

    def FavoriteQuote(self, Task):
        if Task == 1:  # Getter
            return self.FavoriteQuote
        elif Task == 2:  # Setter
            self.favoriteQuote = input("What is this person's favorite quote?")

    def FavoriteQuoteAuthor(self, Task):  # returns or sets the variable depending on the task assigned
        if Task == 1:  # Getter
            return self.favoriteQuoteAuthor
        elif Task == 2:  # Setter
            self.favoriteQuoteAuthor = input("Who is the person that wrote your favorite quote?")

    def Greeting(self):  # greets the user
        print(f"Hi {Basics.GetName()}, my name is {self.name}. I am {self.age} years old. "
              f"My favorite quote at the moment is: {self.favoriteQuote} - By {self.favoriteQuoteAuthor}.")


# list that contains all the "people" in the lounge
Lounge = []

"""
    Functions below, Classes, Imports and Variables above.
"""


def ViewLounge():  # Shows user all the "people" in the lounge
    print(f"Here are all the people in the lounge today {Basics.GetName()}:")
    for People in Lounge:
        print(People.Name(1))
        print(Basics.Border)

    Choice = input("What is the name of the person you would like to meet?: ")  # asks user who they would like to meet

    # determines which person the user wants to "meet"
    for Names in Lounge:
        if Choice == Names.Name(1):
            Names.Greeting()
        else:
            print("Please try spelling the person's name correctly please.")
            ViewLounge()


def CreatePerson():  # allows user to create their own person via the Person class
    print("Welcome to the Person Creator, where you get to play God - no refunds.")

    # asks user for the required variables to initialize the Person class

    Name = input("What would you like the new person's name to be?: ")

    Age = int(input("How old would you like this new person to be?: "))

    FavoriteQuote = input("What is the favorite quote of this new person?: ")

    AuthorOfFQ = input("Who is the author of this person's favorite quote?: ")

    NewPerson = Person(Name, Age, FavoriteQuote, AuthorOfFQ)  # instantiates Person class

    Lounge.append(NewPerson)  # adds new person to the Lounge list

    DialoguePostCreation = ["Press (1) to greet this new person!", "Press (2) to return to the lounge!",
                            "Press any other key to return to the main menu." ]

    for Text in DialoguePostCreation:  # asks user what they would like to do
        print(Text)
    Choice = int(input("What would you like to do?: "))

    if Choice == 1:  # meet the person the user created
        print("Going to meet the new Person now.")
        NewPerson.Greeting()
    elif Choice == 2:  # return to the lounge
        print("Returning to the Lounge")
        ViewLounge()
    else:  # return to the main menu
        print("Returning to Main Menu.")
        Menu.MainMenu()


def EditorMenu():  # menu of the module
    Dialogue = [f"Hi {Basics.GetName()}!", "Welcome to the Revision Lounge, where all the cool code and their "
                "personalities hang out!", "Press (1) to view the list of people here today in the lounge", "Press (2) to create yourself as a person of "
                "code, who also hangs out at the lounge.", "Press any other key to return to the Main Menu"]
    for Text in Dialogue:
        print(Text)

    print(Basics.Border)
    Choice = int(input(f"What would you like to do {Basics.GetName()}?:"))  # asks user what they would like to do

    if Choice == 1:  # takes user to the lounge
        print("Traveling to the Lounge.")
        print(Basics.Border)
        ViewLounge()
    elif Choice == 2:  # takes user to the person creator
        print("Opening the Personality Creator.")
        print(Basics.Border)
        CreatePerson()
    else:  # returns user to main menu
        import Menu
        print("Returning to Main Menu.")
        print(Basics.Border)
        Menu.MainMenu()


def AddPeople():  # 3 people are created as people the user can interact with at the start.
    Person1 = Person("Mike", 24, "The best revenge is massive success", "Frank Sinatra")
    Lounge.append(Person1)

    Person2 = Person("Freddy", 36, "If your ship doesn't come in, swim out to it!", "Jonathan Winters")
    Lounge.append(Person2)

    Person3 = Person("Michelle", 19, "Life is like riding a bicycle. To keep your balance, you must keep moving.", "Albert Einstein")
    Lounge.append(Person3)

    EditorMenu()


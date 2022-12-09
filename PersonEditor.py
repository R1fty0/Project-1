from Data import Basics
Basics = Basics()
class Person:
    def __init__(self, name, age, favoriteQuote, favoriteQuoteAuthor):
        self.name = name
        self.age = age
        self.favoriteQuote = favoriteQuote
        self.favoriteQuoteAuthor = favoriteQuoteAuthor

    def Name(self, Task):
        if Task == 1: # Getter
            return self.name
        elif Task == 2: # Setter
            self.name = input("What would you like to name this person?")

    def GetAge(self):
        return self.age

    def SetAge(self, Age):
        self.age = Age

    def FavoriteQuote(self, Task):
        if Task == 1:  # Getter
            return self.FavoriteQuote
        elif Task == 2:  # Setter
            self.favoriteQuote = input("What is this person's favorite quote?")

    def FavoriteQuoteAuthor(self, Task):
        if Task == 1:  # Getter
            return self.favoriteQuoteAuthor
        elif Task == 2:  # Setter
            self.favoriteQuoteAuthor = input("Who is the person that wrote your favorite quote?")

    def Greeting(self):
        print(f"Hi {Basics.GetName()}, my name is {self.name}. I am {self.age} years old. My favorite quote at the moment is: {self.favoriteQuote} - {self.favoriteQuoteAuthor}.")


def GreetUser():
    Person1 = Person("Bob", 16, "Life is But a Dream", "Mohit")
    print(Person1.Greeting())


GreetUser()
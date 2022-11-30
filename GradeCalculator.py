from Data import GradeCalculator as Stats


def AskForParameters():
    Stats.TotalScore = float(input("What is the Total Amount of Marks avaliable in the course?: "))
    Stats.NumberOfAssignments = float(input("How many assignments did you complete for this course?: "))



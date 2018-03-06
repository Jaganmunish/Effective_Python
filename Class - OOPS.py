# Simple grade empyth classs

"""This is how the basic strucuter of class can be build"""

class SimpleGradeBook(Object):
    def __init__(self):
        pass
    def add_student(self):
        pass
    def report_grade(self):
        pass
    def avg_grade(self):
        pass

#Gradereport Class

"""This is a basic class for report card"""

    class SimpleGradeBook():
        def __init__(self):
            self.grade = {}
        def add_student(self, name):
            self.grade[name] = []
        def report_grade(self, name, score):
            self.grade[name].append(score)
        def avg_grade(self, name):
            avggrade = self.grade[name]
            return sum(avggrade) / len(avggrade)


card = SimpleGradeBook()

card.add_student('Jagatheesh')

card.report_grade('Jagatheesh', 187)

print (card.avg_grade('Jagatheesh'))
x

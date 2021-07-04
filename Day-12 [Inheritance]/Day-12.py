# 30 Days of Code
# Day 12: Inheritance

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        Person.__init__(self,firstName, lastName, idNumber)
        self.score=scores

    def calculate(self):
        sum=0
        for score in scores:
            sum=sum+score
        avrg=sum/len(scores)

        if avrg<40:
            return "T"
        elif avrg>=40 and avrg<55:
            return "D"
        elif avrg>=55 and avrg<70:
            return "P"
        elif avrg>=70 and avrg<80:
            return "A"
        elif avrg>=80 and avrg<90:
            return "E"
        elif avrg>=90 and avrg<=100:
            return "O"


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
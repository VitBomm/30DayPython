def check_letter(a):
    if 90 <= a <= 100:
        return 'O'
    elif 80 <= a < 90:
        return 'E'
    elif 70 <= a < 80:
        return 'A'
    elif 55 <= a < 70:
        return 'P'
    elif 40 <= a < 55:
        return 'D'
    else:
        return 'T'
class Person:
    def __init__(self, firstName, lastName, idNumber):
	    self.firstName = firstName
	    self.lastName = lastName
	    self.idNumber = idNumber
    def printPerson(self):
	    print("Name:", self.lastName + ",", self.firstName)
	    print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName, lastName, idNum)
        self.scores = scores
    def printPerson(self):
        super().printPerson()
    def calculate(self):
        return check_letter(sum(self.scores) / len(self.scores))

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
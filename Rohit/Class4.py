class StudentMarks:
    def __init__(self, sub1, sub2, sub3):
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def result(self):
        average = (self.sub1 + self.sub2 + self.sub3) / 3
        if average >= 40:
            print("Passed")
        else:
            print("Failed")

student = StudentMarks(60, 50, 30)
student.result()



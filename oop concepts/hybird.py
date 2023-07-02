class University:
    def __init__(self, univName):
        self.univName = univName

    def getUniversityDetails1(self):
        print("univName", self.univName)

class Course(University):
    courseName = "CSE"
    def getUniversityDetails2(self):
        print("courseName", self.courseName)

class Batch(Course):
    batchName = 2023
    def getUniversityDetails3(self):
        print("batchName", self.batchName)

class Department(Course, University):
    def __init__(self, univName):
        self.departmentName = "Computer Science"

    def getUniversityDetails4(self):
        print("departmentName", self.departmentName)

obj = Department()

# obj.getUniversityDetails()
obj.getUniversityDetails4()
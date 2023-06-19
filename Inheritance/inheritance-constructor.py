class Father:
    def __init__(self, fatherName):
        self.fatherName = fatherName
        print("father")
class Mother:
    def __init__(self, motherName):
        self.motherName = motherName
        print("mother")
class Son(Father, Mother):
    def __init__(self, sonName, FatherName, motherName):
        self.sonName = sonName
        print("son")
        Mother.__init__(self, motherName)
        Father.__init__(self, FatherName)

    def getFamilyDetails(self):
        print("fatherName",self.fatherName)
        print("motherName", self.motherName)
        print("sonName", self.sonName)


obj1 = Son("sathwick", "sasi", "senthu")

# print()
# print(obj1.sonName)
# print(obj1.fatherName)
# print(obj1.motherName)

obj1.getFamilyDetails()
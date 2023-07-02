class cat:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def info(self):
        print(f"I am a Cat. My name is {self.name}. I am {self.age} years old.")
    
    def makesound(self):
        print("meow")

class cow:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def info(self):
        print(f"I am a Cow. My name is {self.name}. I am {self.age} years old.")
    def makesound(self):
        print("maaaa")

cat1=cat("kutty", 3)
cow1=cow("lakshmi", 4)

for animal in(cat1,cow1):
    animal.makesound()
    animal.info()
    animal.makesound()



        

    

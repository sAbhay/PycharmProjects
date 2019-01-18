memes = 1

testWord = "Zachary Jonah Amiton"

def add(x, y):
    s = x + y
    return s

print(add("memes", " are dreams"))

class Human:
    def __init__(self, age = -10, name = "Bob"):
        self.age = age
        self.name = name

    def greet(self, human):
        print(f"Hello {human.get_name()}, my name is {self.name}, and I am {self.age} years old")

    def get_name(self):
        return self.name

abhay = Human(15, "Abhay")
zack = Human(15, "Zack")

abhay.greet(zack)

for i in range(1, testWord.__len__()+1):
    print(testWord[-i], end="")
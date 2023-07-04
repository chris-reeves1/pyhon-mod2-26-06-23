class Student:
    def __init__(self, name, age, class_="maths"):
        self.name = name
        self.age = age
        self.class_ = class_

    def average_test_score(self, score1, score2, score3):
        average = (score1 + score2 + score3) /300 *100
        return f"{self.name} - average test score: {average}%"

student1 = Student("steve", 10)
print(student1.average_test_score(20, 30, 40))
print(student1)

class Bird:
    def __init__(self, name, wingspan):
        self.name = name
        self.wingspan = wingspan

    def fly(self):
        print(f"{self.name} is flying with a wingspan of {self.wingspan} cm")

    def __str__(self):
        return f"{self.name} ({self.__class__.__name__})"
    
class Owl(Bird):
    def __init__(self, name, wingspan, nocturnal=True):
        super().__init__(name, wingspan)
        self.nocturnal = nocturnal

    def hoot(self):
        print(f"{self.name} is hooting")

    def __str__(self):
        return super().__str__() + f"- nocturnal: {self.nocturnal}"
    
class Dodo(Bird):
    def __init__(self, name, wingspan, extinct=True):
        super().__init__(name, wingspan)
        self.extinct = extinct

    def __str__(self):
        return super().__str__() + f"- extinct: {self.extinct}"
    

bird1 = Bird("eagle", 20)
owl1 = Owl("barn owl", 90)
dodo1 = Dodo("the dodo", 100)

bird1.fly()
print(bird1)

owl1.fly()
owl1.hoot()

print(owl1)

dodo1.fly()
print(dodo1)


# Classes and methods is part oop. object orientated programming. 
# Key concepts:
# class - a blueprint of attributes(variables/args), and methods (functions)
# that we can use through objects of a class.
# object: this is an instance of a class.
# methods: functions internal to a class. 
# allows us to easily make multiple obkects of the same type. 

class Dog: # Creates a class called dog. 
    energy = "high" # setting an attribute for the class

    def speak(self): # creating a method (like a function)
        print("bark")

fido = Dog() # sets an object of class dog called fido.
fido.energy = "low"

print(fido.energy) # calling the attribute energy
fido.speak() # calling the method

class Students:
    pass

student_1 = Students()
student_2 = Students()

print(student_1)

student_1.first = "john"
student_1.last = "smith"
student_1.age = 10

print(student_1.first, student_1.last)

student_2.first = "katie"
student_2.last = "smith"
student_2.age = 12

print(student_2.age)

class Student:
    def __init__(self, first, last, age): # __indicates a background task__
        self.first = first    # init method intitialises the objevt with these attributes.
        self.last = last      # the self param refers to the object itself
        self.age = age        # self maps the class data to the object. 

student_3 = Student("john", "smith", 10)
student_4 = Student("katie", "smith", 12)

print(student_3.age, student_4.age)

class Student1:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last      
        self.age = age
        self.full = first + " " + last


student_5 = Student1("john", "smith", 10)   
print(student_5.full) 


# As a method

class Student2:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last      
        self.age = age

    def fullname(self):
        return(self.first + " " + self.last)

student_6 = Student2("Katie", "smith", 12)

print(student_6.fullname())
print(Student2.fullname(student_6))

# Change to an attribute with a method:

class Students3:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last      
        self.age = age

    def fullname(self):
        return(self.first + " " + self.last)

    def change_age(self):
        self.age = int(self.age + 1)

student_7 = Students3("john", "smith", 10)

print(student_7.age)
student_7.change_age()
print(student_7.age)








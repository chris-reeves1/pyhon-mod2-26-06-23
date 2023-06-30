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

# Self-class variables

class Students4:

    age_increase_amount = 25 # self class variable

    def __init__(self, first, last, age):
        self.first = first
        self.last = last      
        self.age = age

    def fullname(self):
        return(self.first + " " + self.last)

    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

student_8 = Students4("john", "smith", 10)
student_9 = Students4("katie", "smith", 12)
student_8.change_age()
print(student_8.age)
print(student_8.age_increase_amount)
print(Students4.age_increase_amount)

# __dict__

print(Students4.__dict__)
print(student_8.__dict__)
print(student_9.__dict__)

# Change the variable

Students4.age_increase_amount = 20
student_9.age_increase_amount = 15
student_8.change_age()
student_9.change_age()
print(Students4.__dict__)
print(student_8.__dict__)
print(student_9.__dict__)

# Non self class variable

class Students5:

    age_increase_amount = 25 # self class variable
    num_of_students = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last      
        self.age = age

        Students5.num_of_students += 1

    def fullname(self):
        return(self.first + " " + self.last)

    def change_age(self):
        self.age = int(self.age + self.age_increase_amount)

student_10 = Students5("j", "s", 10)
print(Students5.num_of_students)
student_11 = Students5("k", "s", 12)
print(Students5.num_of_students)

# Parent class

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

# Child class

class Cat(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

my_cat = Cat("w", "f", "s")

my_cat.meow()
my_cat.eat()

print(my_cat)

# __str__ method
# Parent class

class Animal1:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        print(f"{self.name} is eating")

    def __str__(self):
        return f"{self.name} ({self.species})"

# Child class

class Cat1(Animal1):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def meow(self):
        print("meow")

    def __str__(self):
        return f"{self.name} ({self.species}, {self.breed})"
    
my_cat1 = Cat1("w", "f", "s")


print(my_cat1)

# __ attribute is only accessible by when calling witht the class name. 
# access by _Classname__attributeName 
# trailing_ its way of using python keywords. class_ input_ 
# _leading underscore - indicates an attribute is private. 

class Feline:
    __family = "something"

cat3 = Feline()

print(cat3._Feline__family)

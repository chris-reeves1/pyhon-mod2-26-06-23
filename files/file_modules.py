# Modules
# Modules are just files, used to extend our functionality. 
# we can import modules, wr can also use our own
# many in-built modules that odnt require set up.
# have modules that need to be installed via pip

#import math # importing the entire module

#number = float(input("enter a number: "))

#answer = math.sqrt(number) # syntax module_name.object_name

#print(answer)

# import multiple modules

#import math
#import random

#def random_pi():
#    return math.ceil(random.randint(1,10) * math.pi)

#for i in range(5):
#    print(random_pi())

# Just with required objects (save memory + perfomance boost)

#from math import pi, ceil, floor
#from random import randint

#def random_pi():
#    return floor(randint(1,10) * pi)

#for i in range(5):
#    print(random_pi())

# pip
# installs modules that require installation
# pypi.org to search for modules
# pip its self need to be installed - hopefully already there on windows
# mac need to use brew (brew also needs to be installed)
# linux - sudo apt install python3-pip
# best to use venv - virtual environment (module 5)

# files:

# read, write, editing with files
# Python supports lots of file types including things like audio, visuals
# but will require modules installed. 
# we will focus on txt files. 

#file = open("filename.txt", "mode") # r (read-only), w (write), r+ (both read and write), a (append).

#file.close() # must close the file when finished - this will close the most recently opened file. 

# To read:
# open the file and use file.readline() - reads a line and moves on to the next.
# read() or readlines() - to read all the lines of the file. 
# seek() - useful to make sure you are reading the correct line file.seek(). 

#eg:

#file = open("example.txt", "r")

#print(file.readline()) # prints 1st
#file.readline() # reads and moves to next line
#print(file.readline()) # prints 3rd line
#files.seek(0) # goes to begining
#print(file.readline()) # prints 1st line

#file.close() # prints 1st, 3rd and 1st.

# eg

#file = open("lines.txt", "r")

#lines = file.readlines() # read all the lines and stored in a lines

#print(lines)
#file.close()

# write a file

#file = open("lines1.txt", "w")

#for n in range(1,11):
#    newline = "this is line" + " " + str(n) + "\n"
#    file.write(newline)

#file.close()


#example

file = open("lines1.txt", "r")

outfile = ""

for line in range(1,10):
    if line % 2 == 0: # takes even numbers
        outfile += file.readline()
    else:
        file.readline() # skip odd numbers

file = open("lines1.txt", "w")
file.write(outfile) # write even numbers
file.close()

# exercise: 
# open a new text file called teams.txt, and add the names of 5 sports teams. 
# read and display the names of the 1st, 4th teams in the files.
# edit the the teams.txt file so that the top line is replaced with "new line"
# print out the edited file line by line. 

file = open("teams.txt", "w")
sports_teams = ["man utd", "man city", "barcelona", "real madrid", "Charlton"]

for i in sports_teams:
    newline = i + "\n"
    file.write(newline)
file.close()

file = open("teams.txt", "r")

lines = file.readlines()

file.close()

#print(lines)
#print(lines[0])
#print(lines[3])
print(lines[0].strip()) # removes the whitespace and also remove \n
print(lines[3].strip())

file = open("teams.txt", "r")

lines = file.readlines()
file.close()

lines[0] = "this is a new line"

file = open("teams.txt", "w")

for i in range(len(lines)):
    if i == len(lines):
        file.write(lines[i]) # checks if last line and no new line char
    else:
        file.write(lines[i].strip() + "\n")
file.close()

file = open("teams.txt", "r")

for line in file:
    print(line.strip())
file.close()

# with statement

with open("filename.txt", "w") as file: #aliasing
    for n in range(1,11):
        newline = "this is line" + " " + str(n) + "\n"
        file.write(newline)

# we dont have to close the file!! 






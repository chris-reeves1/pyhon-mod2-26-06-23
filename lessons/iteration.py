# Iteration is another word for loops, repeating a block code over and over
# without having to write multiple lines.
# saves time. 

# 2 types of loops:
# while loops
# for loops

# While loops
# a while loop will continue to execute code while a conditio is true
# or will exit when another condition is met
# if a condition is never true the while loop would never start

#print("1")
#print("2")
#print("3")
#print("4")

#x = 0 

#while x < 100:
#    print(x)
#    x += 1 # same x = x + 1 

# break

#i = 1

#while i < 6:
#    if i == 3:
#        break
#    print(i)
#    i += 1

# Continue
#j = 0

#while j < 6:
#    j +=1
#    if j == 3:
#        continue
#    print(j)

#k = 1 

#while k < 6:
#    print(k)
#    k +=1
#else:
#    print("k is no longer less than 6")

# while true

#while True:
#    name = input("enter your name: ")
#    if name == "quit":
#        break
#    else:
#        print(f"hello {name}")

# For loops:
# a for loop will iterate over any iterable collection: lists/strings/dictionaires
# useful for when we ewant use data in a collkection
# Do things to individual items in a collection

# Iterating through lists

#my_fruits = ["apple", "orange", "pear"]

#for fruits in my_fruits:
#    print(fruits)

#numbers = [1, 3, 5, 9]

#for item in numbers:
#    print(item)

#l = 0 
#while l < len(numbers):
#    print(numbers[l])
#    l += 1

# Range

for a in range(5):
    print(a) # 0-4 stops at the number

for a in range(1,5):
    print(a) # 1-4 no including 5. 

for a in range(1, 10, 2):
    print(a) # 1-9 in steps of 2.

# string

for letter in "hello":
    print(letter)  

for word in "hello world".split():
    print(word)

# list comprhension
result = [x**2 for x in range(5)]
print(result)

# same as: 

results = []

for x in range(5):
    results.append(x**2)
print(results)

# dictionary iteration

for i in {"drink": "wine"}:
    print(i)

for value in {"food": "jam"}.values():
    print(value)

for key, value in {"shape":"square"}.items():
    print(key, value)

# break and continue

for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(10):
    print(i)
    if i == 5:
        break

#nested loops:

for i in range(1,3):
    for j in range(1,4):
        print(i, "x", j, "=", i*j)

# Write a while loop that asks for the names of 5 people
# for each person print out their name followed by some text "is great"

# counter + while loop, inside while loop have a input, a print and a +=1

counter = 0

while counter < 5:
    name = input("enter your name: ")
    print(name + " is great!")
    counter += 1 

for counter in range(5):
    name = input("Enter your name: ")
    print(name + " is great!")

names = [input("What is your name? ") for name in range(5)]
for name in names: print(f"{name} is awesome!")

[print(f"{name} is awesome!") for name in [input("enter a name? ") for _ in range(5)]]




# Different ways of storing data
# Lists - ordered, mutable, collection of values []
# Dictionaries - unordered, mutable, collections of key-pair values {"Key":"value"}
# Tuples - ordered, immutable, colection of values ()
# Sets - unordered, mutable collection of unique values {"value1", "value2"}

# lists are stored in a variable []

#colours = ["Blue", "red", "green", "yellow"]
#
#print(colours)

#referencing - elements in alist are referenced by the index position
# starts at 0 and -1 going backwards

#print(colours[0])
#print(colours[-4])

#slicing - create a sub-list up to but not including the 2nd number in our range

#print(colours[0:2])
#print(colours[1:])

# altering lists - use index position, need a vlaue, delete with del

#food = ["bread", "cheese", "pasta", "apple"]

#food[0] = "rice"
#del food[1]

#print(food)

# checking if item in a list

#print("pasta" in food)
#print("orange" in food)

# nested lists

#numbers = [1, 2, 3, 4]
#letters = ["a", "b", "c", "d"]

#combined = [numbers, letters]

#print(combined[0][1], combined[1][1])

# multiple data types
#my_list = ["red", 5, ["green", "apple"], 10.5]

#print(my_list)
#print(my_list[2][1])
#print(my_list[0])

# List methods

# append

my_fruits = ["apple", "orange", "kiwi"]
my_fruits.append("pear")
print(my_fruits)

#remove

my_fruits.remove("apple")
print(my_fruits)

# insert

my_fruits.insert(0, "mango")
my_fruits.insert(0, "melon")
print(my_fruits)

# extend (with a list)

my_fruits.extend(["grapes", "cherry"])
print(my_fruits)

# Finding index position

print(my_fruits.index("mango"))

# reversing a list

my_fruits.reverse()
print(my_fruits)

# sorting 

my_fruits.sort()
print(my_fruits)

my_fruits.sort(key=len)
print(my_fruits)

# join

x = ", ".join(my_fruits)
print(x)

# Dictionaries {} key:values pairs
# similar to a list, no indexing. 
# Keys have to have unique values dont. 

drinks = {"fizzy": "sprite", "still": "water", "juice": "orange", "alcohlic": "wine"}
print(drinks)
print(drinks["still"]) # cant query values only keys 

# adding to a dictionary

drinks["non-alcohlic"] = "water"
print(drinks)

# Overwrite 

drinks["non-alcohlic"] = "squash"
print(drinks)

# return all values or keys or both

print(drinks.values())
print(drinks.keys())
print(drinks.items())

print("water" in drinks.values())
print("still" in drinks)

# get method

print(drinks.get("still"))
print(drinks.get("stille", "not found"))
print(drinks.get("stillie"))

# update

drinks.update({"sugary": "cola"})
#or
drinks.update(very_sugary = "red bull")
print(drinks)

# Pop

print(drinks.pop("non-alcohlic"))
print(drinks.pop("non-alcohlic", "not-found"))
print(drinks)

# exercise:

books = {"the handmaiden's tale": ["atwood", "something else"], "the hobbit": "tolkien"}

print(books["the handmaiden's tale"])

# make a dictionary of books, with 3 authors and multiple books per author. 
# use an input() asking for an author name. 
# print back as a string the list of books by the author.
# Use the .join() method.










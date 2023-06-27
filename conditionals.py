# if, elifs, else statements
# conditionals statements are used to accomade different paths our code can follow.
# if statements when a specific condition is met.

my_bool = True

if my_bool:
    print("my bool is true")
else:
    print("my bool is false")

# Nested if statements

#if some_condition:
#    if some other condition:
#        .....
#    else:
#        ....
#else:
#    ......

# conditionals

# equals to: == 
# not equals to: !=
# less than: <
# more than: >
# less than or equals to: <= or >=


# examples

money = 9

if money > 10:
    print("i have some money")
else:
    print("i dont have much money")

# elif - else if
# We dont awlays want to check if every statement equates to true
# mostly only one statement will be true/relevant
# elif makes our code more efficiant
# will only run if no other conditional has been evaluated as true 

temp = 10

if temp >= 30:
    print("its very hot today")
elif temp > 25:
    print("its pretty hot")
elif temp > 20:
    print("its ok")
elif temp > 15:
    print("could be better")
elif temp == 0:
    print("its freezing")
else:
    print("genrally bad weather")

# Exercise:
# ask for an input fron user for a grade/mark
# if the the mark is greater than 85 print "distinction"
# if between 65 and 85 print "pass"
# anything else print "fail"
# if + elif + else 

#x = int(input("enter a grade: "))

#if x >= 85:
#    print("distinction")
#elif x >= 65:
#    print("pass")
#else:
#    print("fail")

# Multiple compareters = with multiple conditions using and/or:

deposit = 0
password = "password"

#if 0 < deposit <= 100 and password == "password":
#    print(f"thank you for £{deposit}")
#else:
#    print("failed to deposit")

#if not (0 < deposit <=100) or password != "password":
#    print("failed to deposit")
#else:
#    print("thank you for the deposit")

# in and not in:

name = "root"

#if name in ("root", "admin", "password"):
#    print("invalid password!")
#else:
#    print("accepted")

if name not in ("root", "admin"):
    print("accepted")
else: 
    print("invalid password")


# challenge:
# weight converter app: convert a user inputted weight(float), and user
# to select either kgs and lbs. write an if statement that checks 
# if the unit is kgs or lbs, if kgs convert into lbs and print the converted value.
# else: to handle the other way around. Error handling for upper/lower case. 






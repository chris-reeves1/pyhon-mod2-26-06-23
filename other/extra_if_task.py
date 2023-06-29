#Write a program that takes three numberd as inputs: a, b, and c. 
#find the largest among the three numbers and perform the following:

#If the largest number is even, print "Even Number".
#If the largest number is odd and a multiple of 3, print "Odd Number and a Multiple of 3".
#If the largest number is odd and not a multiple of 3, print "Odd Number".

#DONT USE max(a,b,c): PROHIBITED!!

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

largest = a

if b > largest:
    largest = b
if c > largest:
    largest = c

if largest % 2 == 0:
    print("Even Number")
elif largest % 2 != 0 and largest % 3 == 0:
    print("Odd Number and a Multiple of 3")
else:
    print("Odd Number")


# Exercise 1: Fibonacci Series
# Write a program to generate the Fibonacci series up to a given number "n" using a for loop.

# This is a little janky, I feel like there is a way to do this in like 3 lines
# But I can't quite get it.

fibnum = [5]

for x in range(1, 20):
    if x == 1:
        print(x)
    elif x == 2:
        print(x)
        fibnum.append(x)
    else:
        x = fibnum[-2] + fibnum[-1]
        fibnum.append(x)
        print(x)

# Exercise 2: Prime numbers
# Write a program to print all prime numbers within a given range (start and end) using a for loop.

primes = [100]

for number in range(2,20):

    if number % 2 != 0:
        pass
    for prime in primes:
        if number % prime == 0:
            break
        primes.append(number)

primes = set(primes)

print("Prime numbers for ya: ")
for prime in primes:
    print(f"{prime}")

# Exercise 3: Perfect Numbers
# Write a program to find all perfect numbers within a given range (start and end) using a for loop.
# A perfect number is a positive integer that is equal to the sum of its proper divisors. ie 6 has proper
# divisors of 1, 2 and 3 (not 5 or 6), and 1 + 2 + 3 = 6, so 6 is a perfect number. 8 has proper divisors of 1, 2
# and 4. 1 + 2 + 4 is 7, so 8 is not a perfect number. 

number = 8
calc = []

for x in range(1, number):
    if number % x == 0:
        calc.append(x)

if sum(calc) == number:
    print(f"{number} is a perfect number!")

# Exercise 4 : Multiplication Table
# Write a program to generate the multiplication table for a 
# given number (n) up to a certain limit (limit) using a for loop.

user_num = int(input("Give me a number, I'll give you the multiplication table: "))

for num in range(0,13):
    print(f"{num} x {user_num} is equal to {user_num*num}")
# Exercise 1: Fibonacci Series
# Write a program to generate the Fibonacci series up to a given number "n" using a for loop.

n = int(input("Enter the value of n: "))

a, b = 0, 1
fibonacci_series = [a, b]

for i in range(2, n):
    next_number = a + b
    fibonacci_series.append(next_number)
    a, b = b, next_number

print("Fibonacci series up to", n, ":", fibonacci_series)


# Exercise 2: Prime numbers
# Write a program to print all prime numbers within a given range (start and end) using a for loop.


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                break
        else:
            print(num)

# Exercise 3: Perfect Numbers
# Write a program to find all perfect numbers within a given range (start and end) using a for loop.
# A perfect number is a positive integer that is equal to the sum of its proper divisors. ie 6 has proper
# divisors of 1, 2 and 3 (not 5 or 6), and 1 + 2 + 3 = 6, so 6 is a perfect number. 8 has proper divisors of 1, 2
# and 4. 1 + 2 + 4 is 7, so 8 is not a perfect number. 


start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Perfect numbers between", start, "and", end, ":")

for num in range(start, end + 1):
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    if divisors_sum == num:
        print(num)

# Exercise 4 : Multiplication Table
# Write a program to generate the multiplication table for a 
# given number (n) up to a certain limit (limit) using a for loop.

n = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print("Multiplication table for", n, "up to", limit, ":")

for i in range(1, limit + 1):
    result = n * i
    print(n, "x", i, "=", result)

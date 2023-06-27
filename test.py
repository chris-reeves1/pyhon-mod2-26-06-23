a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
c = int(input("Enter number 3: "))

if a > b and a > c:
    print("Number 1: ",a,"Is the largest")
    if a % 2 == 0:
        print("Number 1 also even")
    elif a % 3 == 0:
        print("Number 1 is the largest and odd and mutiple of 3")
    else:
        print("Number 1 is the largest and odd and not mutiple of 3")
elif b > a and b > c:
    print("Number 2: ",b,"Is the largest")
    if b % 2 == 0:
        print("Number 2 also even")
    elif b % 3 == 0:
        print("Number 2 is the largest and odd and mutiple of 3")
    else:
        print("Number 2 is the largest and odd and not mutiple of 3")
elif c > a and c > b:
    print("Number 3: ",c,"Is the largest")
    if c % 2 == 0:
        print("Number 3 also even")
    elif c % 3 == 0:
        print("Number 3 is the largest and odd and mutiple of 3")
    else:
        print("Number 3 is the largest and odd and not mutiple of 3")

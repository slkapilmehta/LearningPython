def primeNumber(num):
    if num == 0 or num == 1:
        print("0 and 1 are not prime numbers")
    if num <0:
        print("enter a valid positive number")
    for i in range (2, num):
        if (num%i) == 0:
            print("not a prime number")
            break
    return ("Prime number")

num = -1
print(primeNumber(num))
# Write a function that takes an integer number as a parameter and checks if the number is prime or
# not. A prime number (or a prime) is a natural number greater than 1 and that has no positive
# divisors other than 1 and itself.
import math


def isPrime(n):
    if n < 1:
        return False

    for i in range(2, math.floor(n / 2) + 1):
        if n % i == 0:
            return False

    return True


for t in range(0, 100, 10):
    for i in range(0, 10):
        if isPrime(t + i):
            print("%2i" % (t + i), end=" ")
        else:
            print("## ", end='')
    print()

"""
output:
##  1  2  3 ##  5 ##  7 ## ## 
## 11 ## 13 ## ## ## 17 ## 19 
## ## ## 23 ## ## ## ## ## 29 
## 31 ## ## ## ## ## 37 ## ## 
## 41 ## 43 ## ## ## 47 ## ## 
## ## ## 53 ## ## ## ## ## 59 
## 61 ## ## ## ## ## 67 ## ## 
## 71 ## 73 ## ## ## ## ## 79 
## ## ## 83 ## ## ## ## ## 89 
## ## ## ## ## ## ## 97 ## ## 
"""

# Write a program that computes the factorial of an integer input number using a self-defined
# function âfactâ such that:
#
#       ð
# n! =  â ð
#      ð=1
#
# Use a for-loop in the function to perform the calculation. Do not use a recursive function.

def fact(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


print(fact(1))
print(fact(10))
print(fact(50))
print(fact(-1))

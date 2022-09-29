# Write a program that reads a strictly positive integer number n and prints the sum
# 1+2+3+4+…+n.

number = int(input("Enter a strictly positive integer: "))

if number <= 0:
    exit(1)

sm = number
for i in range(1, number):
    sm += i

print(f"The sum is {sm}")

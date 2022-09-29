# Write a program that reads five integers from the console, determines the smallest of those
# numbers after reading in each new number and prints the smallest at the end. You can program
# this efficiently using only two variables. Do not use loops for this assignment!

smallest_number: int = int(input("Enter integer 1: "))

number = int(input("Enter integer 2: "))
if number < smallest_number:
    smallest_number = number

number = int(input("Enter integer 3: "))
if number < smallest_number:
    smallest_number = number

number = int(input("Enter integer 4: "))
if number < smallest_number:
    smallest_number = number

number = int(input("Enter integer 5: "))
if number < smallest_number:
    smallest_number = number

print(f"The smallest number is {smallest_number}")

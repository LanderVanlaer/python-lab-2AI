# Write a program that asks for 3 integers that represent the current date, next asks for 3 integers
# that represent a date of birth. Then the program has to calculate the person’s age and prints it in
# years and months.
# Example:
#       Current date: 22 1 2006
#       Date Of Birth: 25 1 1987
#       Your age is 18 years and 11 months

current_date = input("Current date: ").split()
date_birth = input("Date Of Birth: ").split()

days = int(current_date[0]) - int(date_birth[0])
month = int(current_date[1]) - int(date_birth[1])
years = int(current_date[2]) - int(date_birth[2])

if days < 0:
    month -= 1

if month < 0:
    month = 11
    years -= 1

print(f"Your age is {years} years and {month} months")

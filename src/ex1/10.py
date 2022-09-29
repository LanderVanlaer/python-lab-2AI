# Write a program that asks 5 integer numbers and prints the average after each entry using 2
# decimal places. Do not use loops for this assignment and use 4 variables at most!
#
# Example:
#       Enter integer number 1: 10
#       Average: 10.0
#       Enter integer number 2: 20
#       Average: 15.0
#       Enter integer number 3: 15
#       Average: 15.0
#       Enter integer number 4: 20
#       Average: 16.25
#       Enter integer number 5: 30
#       Average: 19.0

avg = int(input("Enter integer number 1: "))
print(f"Average: {round(avg / 1, 2)}")
avg += int(input("Enter integer number 2: "))
print(f"Average: {round(avg / 2, 2)}")
avg += int(input("Enter integer number 3: "))
print(f"Average: {round(avg / 3, 2)}")
avg += int(input("Enter integer number 4: "))
print(f"Average: {round(avg / 4, 2)}")
avg += int(input("Enter integer number 5: "))
print(f"Average: {round(avg / 5, 2)}")

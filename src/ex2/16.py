# Write a program that reads an integer limit. Next, the program will keep asking integers until the
# sum of these numbers is greater than or equal to the limit. Use only 2 variables!
# Example:
#       Integer limit: 23
#       9
#       12
#       4
#       Limit achieved or crossed

limit = int(input("Enter the limit: "))
total = 0

while total < limit:
    total += int(input())

print("Limit achieved or crossed")

# Write a program that reads two integers on one line from the console and prints these on the next
# line using a phrase such as demonstrated below.
#
# Example:
#       Enter two integers: 17 7
#       The integers are 17 and 7

a, b = input("Enter two integers: ").split()
print(f"The integers are {a} and {b}")

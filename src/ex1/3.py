# Write a program that reads two integers on one line from the console and prints the sum and
# product on the next line.
#
# Example:
#       Enter two integers: 2 3
#       Sum: 5
#       Product: 6

a, b = input("Enter two integers: ").split()
a = int(a)
b = int(b)
print(f"Sum: {a + b}\n"
      f"Product: {a * b}")

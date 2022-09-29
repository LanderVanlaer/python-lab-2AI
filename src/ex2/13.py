# Write a program that prints the numbers -3, -1, 1, 3, 5, …, 25 on a single line, separated by a
# comma and a blank space. The program does not read user input and uses only 1 variable!
# Tip: use the end keyword in the print() statement.

for i in range(-3, 25, 2):
    print(i, end=", ")
print(25)

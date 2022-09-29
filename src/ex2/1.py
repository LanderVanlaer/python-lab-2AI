# Write a program that reads an integer from the console, stores it in a variable and prints whether it
# is even or odd.

integer = int(input("Enter an integer: "))

if integer % 2 == 0:
    print("Even")
else:
    print("Odd")

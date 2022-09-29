# Write a program that reads a real number from the console, stores it in a variable and prints
# whether it is positive, negative or equal to zero.

number = float(input("Enter a number: "))

if number == 0:
    print("Equal to zero")
elif number > 0:
    print("Positive")
else:
    print("Negative")

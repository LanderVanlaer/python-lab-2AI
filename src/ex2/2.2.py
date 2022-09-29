# Write a program that reads a real number from the console and prints if it is part of the interval
# [5,10[ = { x ∈ ℝ | 5 ≤ x < 10}

integer = float(input("Enter a number: "))

if 5 <= integer < 10:
    print("Part")
else:
    print("Not part")

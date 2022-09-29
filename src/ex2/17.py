# Write a program that reads a real number in the range [-2, 4.5[ and prints it. If the number
# entered is not in this range the program must ask it again until that condition is met.

number = float(input("Enter a number: "))

while not (-2 <= number < 4.5):
    number = float(input("Enter a new number: "))

print(number)

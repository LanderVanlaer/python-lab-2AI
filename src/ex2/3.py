# Write a program that reads a real number from the console and prints for every following condition
#
# if it satisfies that condition:
#       ConditionA: 3≤x<8,5
#       ConditionB: x<3 or 5,4<x≤7,3 or x>13
#       ConditionC: x≠3 and x<9,75
# Example:
#       0 does not satisfy A, but does satisfy B and C
#       3 satisfies A, but does not satisfy B or C
#       8 satisfies A, does not satisfy B but satisfies C
#       15 does not satisfy A, satisfies B but does not satisfy C

number = float(input("Enter a number: "))

a = 3 <= number < 8.5
b = number < 3 or 5.4 < number <= 7.3 or number > 13
c = number != 3 and number < 9.75

if a:
    if b:
        if c:
            print(f"{number} satisfies A, B and C")
        else:
            print(f"{number} satisfies A and B but not C")
    else:
        if c:
            print(f"{number} satisfies A, does not satisfy B but satisfies C")
        else:
            print(f"{number} satisfies A, but does not satisfy B or C")
else:
    if b:
        if c:
            print(f"{number} does not satisfy A, but does satisfy B and C")
        else:
            print(f"{number} does not satisfy A, satisfies B but does not satisfy C")
    else:
        if c:
            print(f"{number} does not satisfy A or B but satisfies C")
        else:
            print(f"{number} does not satisfy A, B or C")

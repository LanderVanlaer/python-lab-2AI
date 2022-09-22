# Write a program that reads two integers and prints the integer quotient, the real quotient and the
# remainder.
#
# Example:
#       Input: 11 4
#       Integer quotient: 2
#       Quotient: 2.75
#       Remainder: 3

a, b = input("Input: ").split()
a = int(a)
b = int(b)
print(f"""Integer quotient: {a // b}
Quotient: {a / b}
Remainder: {a % b}
""")

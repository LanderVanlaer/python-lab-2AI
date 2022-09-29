# Expand the previous program so the real quotient is also printed using two decimal places.
# remainder.
#
# Example:
#       Input: 10 3
#       Integer quotient: 3
#       Quotient: 3.3333333333333335
#       Remainder: 1
#       quotient (2decimal places): 3.33

a, b = input("Input: ").split()
a = int(a)
b = int(b)
print(f"""Integer quotient: {a // b}
Quotient: {a / b}
Remainder: {a % b}
quotient (2decimal places): {round(a / b, 2)}
""")

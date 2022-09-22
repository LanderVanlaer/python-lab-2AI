# Write a program that asks an integer value and prints that value as a decimal,
# hexadecimal and octal value

value = int(input("Enter an integer: "))
print(f"{value} {hex(value)} {oct(value)}")

# Repeat the previous exercise, but make use of
#       number1,operand,number2 = input(“Input: ”).split()
# to read the entries from one line.
# Example:
#       Input: 245 + 16
#       Output: 245.00 + 16.00 = 261.00
#
#       Input: 245 / 123.45
#       Output: 245.00 / 123.45 = 1.98

string = input().split()
num1 = float(string[0])
operand = string[1]
num2 = float(string[2])

match operand:
    case "+":
        print(f"{num1} + {num2} = {round(num1 + num2, 2)}")
    case "-":
        print(f"{num1} - {num2} = {round(num1 - num2, 2)}")
    case "*":
        print(f"{num1} * {num2} = {round(num1 * num2, 2)}")
    case "/":
        print(f"{num1} / {num2} = {round(num1 / num2, 2)}")

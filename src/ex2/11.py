# Write a program that reads an entry such as:,
#       number1
#       operand
#       number 2
# (where number 1 and number2 are real numbers and the operand is + - * or /) and prints the input
# along with the calculated output (using 2 decimal places).
# Example:
#       Input:
#           245
#           +
#           16
#       Output:
#           245 + 16 = 261.00

num1 = float(input())
operand = input()
num2 = float(input())

match operand:
    case "+":
        print(f"{num1} + {num2} = {round(num1 + num2, 2)}")
    case "-":
        print(f"{num1} - {num2} = {round(num1 - num2, 2)}")
    case "*":
        print(f"{num1} * {num2} = {round(num1 * num2, 2)}")
    case "/":
        print(f"{num1} / {num2} = {round(num1 / num2, 2)}")

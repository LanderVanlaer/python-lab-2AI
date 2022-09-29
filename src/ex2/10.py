# Write a program that reads a digit (0,1,…,9) and prints it as a text string. If the input is not a digit,
# an error message should be printed.
# Example:
#       Input: 3
#       Output: ‘drie’
#
#       Input: 23
#       Output: 23 is not a digit

digit = int(input("Enter a digit: "))
match digit:
    case 0:
        print("Nul")
    case 1:
        print("Een")
    case 2:
        print("Twee")
    case 3:
        print("Drie")
    case 4:
        print("Vier")
    case 5:
        print("Vijf")
    case 6:
        print("Zes")
    case 7:
        print("Zeven")
    case 8:
        print("Acht")
    case 9:
        print("Negen")
    case _:
        print("Does not recognize digit")

# Write a program to get a string made of the first 2 and the last 2 chars from a string obtained from
# user input. If the string length is less than 2, return “empty string”.
# Example:
#       Input: ‘Bananas’
#       Output: ‘Baas’
#       Input: ‘Ba’
#       Output: ‘BaBa’
#       Input: ‘B’
#       Output: ‘empty string’

s = input("Input: ")
if len(s) >= 2:
    print(s[0:2] + s[-2:])
else:
    print("empty string")

# Write a program that asks input from the user and displays that input back in upper and lower
# cases.
# Example:
#       What is your favorite scripting language? Python
#   Output:
#       Your favorite scripting language is PYTHON
#       Your favorite scripting language is python

s = input("What is your favorite scripting language? ")

print("Your favorite scripting language is " + s.upper())
print("Your favorite scripting language is " + s.lower())

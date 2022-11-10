# Write a function ‘checkpasswd’ that parses a string using several regular expressions to check for
# password validity. The password is only valid if:
# - It contains at least 8 characters
# - It has at least one uppercase character
# - It has at least one lowercase character
# - It contains one or more digits
# - It has at least 2 special characters (!, $, &, etc.)
#
# For the sake of simplicity, an underscore counts as a regular character (not a special character).
# Test your function by parsing the list below. Print each list item, followed by ‘Valid’ or ‘Invalid’
# depending on the function’s return value (which should be True or False). Remember that
# re.search() is ‘truthy’!
#
# passwords = ['ABCD', 'ABCDEFGH', 'ABcdEFgh', 'ABcd1234', 'ABcd12!&']
#
# Output:
#   ABCD: Invalid
#   ABCDEFGH: Invalid
#   ABcdEFgh: Invalid
#   ABcd1234: Invalid
#   ABcd12!&: Valid
import re

passwords = ['ABCD', 'ABCDEFGH', 'ABcdEFgh', 'ABcd1234', 'ABcd12!&']


def checkpasswd(s: str):
    return re.match(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[\!\$\&]).{8,}$", s)


for p in passwords:
    print(f"{p}: {'valid' if checkpasswd(p) else 'invalid'}")

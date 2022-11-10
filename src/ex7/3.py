# Write a function ‘maskCC’ that only prints the last 4 digits of a credit card number and changes the
# other numbers into ‘X’ using regular expressions. You are obliged to work with the groups method
# AND substitution by function.
# Make sure the function works for non-separated digits, groups of 4 digits separated by a space
# and groups of 4 digits separated by a hyphen or a combination thereof using the same regular
# expression.
# The output format should always be the form used in the example.
#
# Example:
#   Input: 1234567812345678
#   Output: XXXX XXXX XXXX 5678
#
#   Input: 1234 5678 1234 5678
#   Output: XXXX XXXX XXXX 5678
#
#   Input: 1234-5678-1234-5678
#   Output: XXXX XXXX XXXX 5678
#
#   Input: 1234 5678-12345678
#   Output: XXXX XXXX XXXX 5678
import re


# noinspection PyPep8Naming
def maskCC(s: str):  # NOSONAR
    return re.sub(r"^(?:\d{4}[ -]?){3}(\d{4})$", r"XXXX XXXX XXXX \1", s)


print(f"'1234567812345678' -> {maskCC('1234567812345678')}")
print(f"'1234 5678 1234 5678' -> {maskCC('1234 5678 1234 5678')}")
print(f"'1234-5678-1234-5678' -> {maskCC('1234-5678-1234-5678')}")
print(f"'1234 5678-123456678' -> {maskCC('1234 5678-12345678')}")

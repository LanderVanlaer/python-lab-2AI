# 0 Write a function ‘checkSSN’ WITHOUT using regular expressions to detect a valid social security
# number format (xx.xx.xx-xxx.xx). You DO NOT have to check if the first three values form a
# realistic date of birth (e.g. months can be > 12, etc.). If valid, return True, else return False.
#
# Example:
#   print(checkSSN(‘00.11.22-345.67’))
#   >>>True
#   print(checkSSN (‘00112234567’))
#   >>>False

# noinspection PyPep8Naming
def checkSSN(s: str):  # NOSONAR
    return s[:2].isnumeric() and s[2] == '.' \
           and s[3:5].isnumeric() and s[5] == '.' \
           and s[6:8].isnumeric() and s[8] == '-' \
           and s[9:12].isnumeric() and s[12] == '.' \
           and s[13].isnumeric()


print(checkSSN('00.11.22-345.67'))  # True
print(checkSSN('00112234567'))  # False

# Repeat the previous assignment, but this time use regular expressions

import re


# noinspection PyPep8Naming
def checkSSN(s: str):  # NOSONAR
    return re.match(r'^(\d{2}\.){2}\d{2}-\d{3}\.\d{2}$', s) is not None


print(checkSSN('00.11.22-345.67'))  # True
print(checkSSN('00112234567'))  # False

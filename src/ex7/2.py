#  Write a function ‘snake’ to extract the word ‘python’ out of a string using regular expressions,
# where ‘python’ has to be detected in every possible variant. Valid variants could be (nonexhaustive list):
#   python
#   Python
#   PYTHON
#   PyThOn
#   …
import re


def snake(s: str):
    arr = list(re.findall("python", s, flags=re.IGNORECASE))
    return arr[0] if len(arr) > 0 else ''


print(f"'bagpythonreward' -> '{snake('bagpythonreward')}'")
print(f"'guidePythonwool' -> '{snake('guidePythonwool')}'")
print(f"'churchPYTHONhurrah' -> '{snake('churchPYTHONhurrah')}'")
print(f"'whitenPyThOnpencil' -> '{snake('whitenPyThOnpencil')}'")
print(f"'whitenPyhOnpencil' -> '{snake('whitenPyhOnpencil')}'")

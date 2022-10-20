# Define a function “findCommon” which can return common items from 2 lists (these are passed as
# arguments). Use a single line of code in the function. Hint: use the set() function!
# Example:
#       a = ['computer', 'mouse', 'printer', 'safari']
#       b = ['safari', 'lion', 'elephant', 'mouse', 'rhino']
#       print(findCommon(a,b))
#       Output: {'safari', 'mouse'}


def findCommon(a, b):  # NOSONAR
    return set(a) & set(b)


a = ['computer', 'mouse', 'printer', 'safari']
b = ['safari', 'lion', 'elephant', 'mouse', 'rhino']

print(findCommon(a, b))

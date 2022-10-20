# Write a program to combine two dictionaries, adding values for identical keys.
# Example:
#       d1 = {'a': 10, 'b': 20, 'c':30}
#       d2 = {'a': 30, 'b': 20, 'd':40}
#       Output: {‘a’:40, ’b’:40, ’c’:30, ‘d’:40}

d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'a': 30, 'b': 20, 'd': 40}

print({k: d1.get(k, 0) + d2.get(k, 0) for k in d1.keys() | d2.keys()})

# Write a program to merge two dictionaries. Hint: use the copy() method.
# Example:
#       d1 = {'a': 10, 'b': 20}
#       d2 = {'x': 30, 'y': 20}
#       Output: {'a': 10, 'b': 20, 'x': 30, 'y': 20}

d1 = {'a': 10, 'b': 20}
d2 = {'x': 30, 'y': 20}

d = d1.copy()
d.update(d2)

print(d)

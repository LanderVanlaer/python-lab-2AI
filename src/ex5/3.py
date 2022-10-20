#  Write a program to sum all the values in a dictionary.
# Example:
#       d = {‘data1’:110,’data2’:-30,’data3’:139}
#       Output: 219

d = {"data1": 110, "data2": -30, "data3": 139}

sm = 0
for v in d.values():
    sm += v

print(sm)

# Write a program to concatenate the following dictionaries to create a new one using a for loop with
# a single line of code and then print it:
# d1 = {1:1,2:2}
# d2 = {3:3,4:4}
# d3 = {5:5,6:6}

d1 = {1: 1, 2: 2}
d2 = {3: 3, 4: 4}
d3 = {5: 5, 6: 6}

# Way 1
dc1 = {}
for d in (d1, d2, d3):
    for k, v in d.items():
        dc1[k] = v
print(dc1)

# Way 2
dc2 = {}
for d in (d1, d2, d3):
    dc2.update(d)
print(dc2)

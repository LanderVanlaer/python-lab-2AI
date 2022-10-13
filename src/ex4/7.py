# Write a program to generate and print a tuple whose values are even numbers in the interval
# [0,10].

print(tuple([x for x in range(0, 11) if x % 2 == 0]))

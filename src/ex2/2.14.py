# 4 Write a program that asks for a digit (1..9) and prints its multiplication table (from 1 to 20 times
# the integer). Make sure each column is aligned properly.
# Example:
#       Integer input [1..9]: 9
#       1 x 9 = 9
#       2 x 9 = 18
#       3 x 9 = 27
#       4 x 9 = 36
#       …
#       18 x 9 = 162
#       19 x 9 = 171
#       20 x 9 = 180

digit = int(input("Integer input [1..9]: "))

for i in range(1, 21):
    print("%2d x %d = %3d" % (i, digit, i * digit))

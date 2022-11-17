# Write a program that appends a random integer from 0 to 9 (included) to a file ‘randomadd.txt’
# each time this program runs. Make sure that every addition is placed on another line

from random import randrange

with open("randomadd.txt", 'a') as f:
    f.write(str(randrange(10)) + "\n")

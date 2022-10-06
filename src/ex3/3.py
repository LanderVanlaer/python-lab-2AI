# Write a function “printLongest” that has 2 strings as arguments and prints the longest string using
# the len() function. If both strings are equally long, the function should print both strings line by line.

def printLongest(str1, str2):
    if (len(str1) >= len(str2)):
        print(str1)
    if (len(str2) >= len(str1)):
        print(str2)


printLongest("Longer", "Long")
printLongest("Small", "normal")
printLongest("Hello", "World")

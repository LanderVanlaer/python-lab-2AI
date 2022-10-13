# Write a program that accepts a comma separated sequence of 5 strings as input and prints the
# strings in a comma-separated sequence after sorting them alphabetically. Make sure this works for
# capitalized and lowercase strings.

strings = input("Enter comma separated sequence of 5 strings: ")
lst = strings.split(',')
lst.sort()
strings = ','.join(lst)
print(strings)

# Write a function to create a Caesar encryption. A Caesar cipher is one of the simplest and most
# widely known encryption techniques. It is a type of substitution cipher in which each letter in the
# plaintext is replaced by a letter some fixed number of positions down the alphabet. For example,
# with a right shift of 3, A would be replaced by D, B would become E, and so on. The method is
# named after Julius Caesar, who used it in his private correspondence. Use a list to compose the
# encrypted text and transform the complete list into a string using “join” to print it.
# Example:
#   Input: abc
#   Output: def

def ceasar_encryption(s: str):
    return "".join([chr(ord(c) + 3) for c in s])


print(ceasar_encryption("abc"))
print(ceasar_encryption("ABC"))
print(ceasar_encryption("xyz"))

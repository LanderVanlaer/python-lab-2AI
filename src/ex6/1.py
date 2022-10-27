# Write a function “delChar” to remove the n-th index character from a string. If the string is not at
# least n characters long, print an error message.
# Example:
#       delChar(‘Python’,0) -> ‘ython’
#       delChar(‘Python’,2) -> ‘Pyhon’
#       delChar(‘Python’,127) -> ‘String not long enough’

def delChar(s: str, n: int):
    if n >= len(s):
        return "String not long enough"
    return s[:n] + s[n + 1:]


print(delChar('Python', 0))
print(delChar('Python', 2))
print(delChar('Python', 127))

# Write a function “tagMe” to create a string with HTML tags around the word(s).
# Example:
#       tagMe('Python', ‘i’) -> '<i>Python</i>'
#       tagMe('Python', ‘b’) -> '<b>Python</b>'

def tagMe(s: str, c: str):
    return f"<{c}>{s}</{c}>"


print(tagMe('Python', 'i'))
print(tagMe('Python', 'b'))

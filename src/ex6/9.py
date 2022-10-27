# Write a program to decode a secret message. The encoder from which you received the secret
# message flips the message backwards and inserts non-alphabetic characters in the message to
# make it hard to decipher. You will therefore need to create a program that will take the encoded
# message as an input string, flip it around, remove any characters that are not a letter or a space
# and output the hidden message.
# Example:
#   Input: d32%l+*r53o9W!* o-l=789le%H
#   Output: Hello World
txt = "d32%l+*r53o9W!* o-l=789le%H"
print("".join([c for c in txt[::-1] if c.isalpha() or c == " "]))

# Write a program that asks the user a sentence and prints each word from that sentence rightjustified.
# The longest word should start at the first cursor position of its line, the other words should
# adapt. If the user enters whitespaces before or after the string, they should be removed.
# Example:
#       Enter sentence:     This is a nice sentence
#   Output:
#      This
#        is
#         a
#      nice
#  sentence

s = input("Enter sentence: ")

words = s.split()

max_length = max([len(w) for w in words])

for w in words:
    print(w.rjust(max_length))

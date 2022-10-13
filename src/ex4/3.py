# 3 Write a function “removeFromList” that has a list and a string as arguments. If the string is present
# in the list, all the occurences of this string have to be removed from the list. The function has to
# return the number of removed strings. Finally, print the list and that number.
# Example:
#       spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
#       removeFromList(spam, 'cat')
#       3 entries deleted
#       ['bat', 'rat', 'hat']


# noinspection PyPep8Naming
def removeFromList(lst: list, s: str):  # NOSONAR
    delete_count = 0

    try:
        while True:
            lst.remove(s)
            delete_count += 1
    except ValueError:
        return delete_count


spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
print(f"{removeFromList(spam, 'cat')} entries deleted")
print(spam)

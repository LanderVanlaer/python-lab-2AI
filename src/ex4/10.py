# Define a function “printList” which can generate and print a list where the values are the square of
# all even numbers between 1 and 20 (both included) using list comprehension in a single line of
# code.

def printList():
    return [x ** 2 for x in range(1, 21) if x % 2 == 0]


print(printList())

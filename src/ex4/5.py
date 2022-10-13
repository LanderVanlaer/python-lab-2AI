# Define a function “printList” which can generate and print a list where the values are the square of
# numbers between 1 and 20 (both included) without using list comprehension.

def printList():
    lst = []

    for i in range(1, 21):
        lst.append(i ** 2)

    return lst


print(printList())

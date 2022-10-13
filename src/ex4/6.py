# Expand the previous function using two integer arguments to specify the start and stop index from
# which to print (stop index included!). Print the result as a tuple.
# Example: printList(3,7) should print: (16, 25, 36, 49)

def printList(num1: int, num2: int):
    lst = []

    for i in range(num1 + 1, num2 + 1):
        lst.append(i ** 2)

    return tuple(lst)


print(printList(3, 7))

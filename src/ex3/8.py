# Make use of the previous function to write a function to find the maximum of 3 integers.

def maximum(a, b, c):
    if b < a > c:
        return a
    if b > c:
        return b
    return c


print(maximum(1, 2, 3))
print(maximum(3, 2, 1))
print(maximum(2, 3, 1))
print(maximum(0, 0, 0))

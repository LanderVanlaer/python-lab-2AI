# Write a program which takes 2 digits, X,Y as input and generates a 2D array. The element value in
# the i-th row and j-th column of the array should be i*j.
# Example:
#       Input: 3,5
#       Output: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

n1 = int(input("Num 1: "))
n2 = int(input("Num 2: "))

lst = []

for i in range(0, n1):
    sublst = []

    for j in range(0, n2):
        sublst.append(j * i)

    lst.append(sublst)

print(lst)

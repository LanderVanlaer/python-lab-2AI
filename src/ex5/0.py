# Write a program that asks for an integer number n and generates a dictionary that contains {i: i*i}
# with i an integral number between 1 and n (both included). The program should print the dictionary
# as well.
#
# Example:
#       Input: 8
#       Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}


n = int(input("Enter an integer: "))

dc = {}

for i in range(1, n + 1):
    dc[i] = i ** 2

print(dc)

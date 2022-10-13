# Write a program that asks for 5 integer numbers (line by line). After each entry, print the sorted list.
# Make sure the program does not crash for a non-integer or non-numeric input. Regardless of
# these incorrect entries, the program has to keep asking integer numbers until 5 valid values were
# submitted.

lst = []

for i in range(1, 6):
    while True:
        inp = input(f"Enter number ({i}): ")
        if inp.isnumeric():
            lst.append(int(inp))
            break

lst.sort()

for n in lst:
    print(n, end=", ")

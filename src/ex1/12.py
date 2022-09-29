# A voltage U is applied to 2 series resistors R1 and R2. The current I can be found (using Ohm's
# law) as: 𝐼 = U/(R1+r2). The voltage U2 over resistor R2 is I.R2. Write a program that reads the values
# of U, R1 and R2 and calculates and prints I and U2 on a single line.
#
# Example:
#       Enter U[V]: 10
#       Enter R1[Ohm]: 5000
#       Enter R2[Ohm]: 5000
#       I = 0.001000 A, U2 = 5.000000 V

u = int(input("Enter U[V]: "))
r1 = int(input("Enter R1[Ohm]: "))
r2 = int(input("Enter R2[Ohm]: "))

i = u / (r1 + r2)
print(f"I = {i} A, U2 = {i * r2} V")

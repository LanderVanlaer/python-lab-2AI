# Write a program that asks the user to enter the radius of a circle and prints the surface of that
# circle. Use PI as a variable equal to 3.141592653589793.

import math

radius = float(input("radius: "))
print(f"surface: {radius ** 2 * math.pi}")

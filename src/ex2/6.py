# Write a program that compares your speed with the speed limit. If you are not speeding, there is
# no problem. If you are speeding, it will calculate and print your fine (use 2 decimal places). The
# fine is a fixed amount of €100 plus €2,5 per km/h you were speeding.
# Example:
#       Enter your speed: 131
#       Enter speed limit: 120
#       You were speeding 11km/h and have to pay 127.50 Euro

speed = int(input("Enter your speed: "))
speed_limit = int(input("Enter speed limit: "))

if speed < speed_limit:
    print("You were not speeding")
else:
    print(f"You were speeding {speed - speed_limit}km/h"
          f"and have to pay {round(100 + (speed - speed_limit) * 2.5, 2)} Euro")

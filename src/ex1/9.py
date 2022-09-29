# Write a program that asks the user to enter an integer number of seconds and prints how many
# days, hours, minutes and seconds this represents (do not use loops for this exercise)
#
# Example:
#       Enter a number of seconds: 86399
#       86399 seconds is 0 days, 23 hours, 59 minutes and 59 seconds

MINUTE_IN_SECONDS = 60
HOUR_IN_SECONDS = MINUTE_IN_SECONDS * 60
DAY_IN_SECONDS = HOUR_IN_SECONDS * 24

totalSeconds = int(input("Enter a number of seconds: "))
totalSecondsCpy = totalSeconds

days = totalSeconds // DAY_IN_SECONDS
totalSeconds %= DAY_IN_SECONDS

hours = totalSeconds // HOUR_IN_SECONDS
totalSeconds %= HOUR_IN_SECONDS

minutes = totalSeconds // MINUTE_IN_SECONDS
totalSeconds %= MINUTE_IN_SECONDS

print(f"{totalSecondsCpy} seconds is {days} days, {hours} hours, {minutes} minutes and {totalSeconds} seconds")

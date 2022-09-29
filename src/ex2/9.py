# 9 Write a program that reads two times (expressed in hh mm ss) and calculates and prints the time
# difference expressed as hh hours mm minutes ss seconds. If the start time is later than the stop
# time you may assume that the start time started one day earlier.
# Example:
#       Start time:     2 12 12     3 12 18     5 23 45     21 0 0
#       Stop time:      3 15 17     3 15 17     7 10 30     4 30 15
#       Difference:     1 3 5       0 2 59      1 46 45     7 30 15


time_start = input("Start time: ").split()
time_stop = input("Stop time: ").split()

hh = int(time_stop[0]) - int(time_start[0])
mm = int(time_stop[1]) - int(time_start[1])
ss = int(time_stop[2]) - int(time_start[2])

if ss < 0:
    mm -= 1
    ss += 60

if mm < 0:
    hh -= 1
    mm += 60

if hh < 0:
    hh += 24

print(f"Difference: {hh}\t{mm}\t{ss}")

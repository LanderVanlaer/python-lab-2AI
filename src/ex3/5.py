# Write a function that reads an integer number, compute 45 divided by that number and use
# try/except to catch the exceptions. Test this using numbers different from 0 and using 0 itself.

def divide45by(n):
    try:
        print(f"45 / {n} = {45 / n}")
    except ZeroDivisionError:
        print("Can not divide by zero (0)")


divide45by(45)
divide45by(10)
divide45by(100)
divide45by(1)
divide45by(0)

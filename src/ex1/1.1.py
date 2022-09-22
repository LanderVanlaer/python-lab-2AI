# Write a program that prints the variable type of three variables.
# Example: a=2 b=3.0 c='myName'
#   Output:
#       2 is of type <class 'int'>
#       3.0 is of type <class 'float'>
#       myName is of type <class 'str'>

a = 2
b = 3.0
c = "myName"

print(f"{a} is of type {type(a)}")
print(f"{b} is of type {type(b)}")
print(f"{c} is of type {type(c)}")

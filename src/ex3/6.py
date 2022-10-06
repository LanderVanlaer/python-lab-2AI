# Write a program that computes the factorial of an integer input number using a self-defined
# function “fact” such that:
#
#       𝑛
# n! =  ∏ 𝑘
#      𝑘=1

def fact(n):
    return 1 if n <= 0 else fact(n - 1) * n


print(fact(1))
print(fact(10))
print(fact(50))
print(fact(-1))

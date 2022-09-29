# Write a program that asks an integer amount of Euro’s (e.g. 888) and prints what bills
# (500,200,100,50,20,10,5) and coins (2,1) this represents. Use only one variable!

amount = int(input("Enter an integer amount of Euro's: "))

print(f"500 x {amount // 500}")
amount %= 500
print(f"200 x {amount // 200}")
amount %= 200
print(f"100 x {amount // 100}")
amount %= 100
print(f"50 x {amount // 50}")
amount %= 50
print(f"20 x {amount // 20}")
amount %= 20
print(f"10 x {amount // 10}")
amount %= 10
print(f"5 x {amount // 5}")
amount %= 5
print(f"2 x {amount // 2}")
amount %= 2
print(f"1 x {amount}")

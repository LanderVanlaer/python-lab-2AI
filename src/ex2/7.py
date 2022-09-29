# Write a program that calculates and prints your BMI (Body Mass Index). BMI is a measure for
# determining possible overweight. The ideal BMI is between 20 and 25. If your BMI is over 25, you
# are overweighed. A BMI under 20 means you are under your “normal” weight.
# BMI=(weight in kg)/(size in m)².

weight = float(input("Enter your weight (kg): "))
size = float(input("Enter size (m): "))
bmi = weight / size ** 2

print(f"Your BMI is {bmi}")

if bmi < 20:
    print("Under \"Normal\" weight")
elif bmi < 25:
    print("ideal")
else:
    print("Overweighed")

height = float(input("Enter you height in Meters: \n"))
weight = int(input("Enter your weight in KiloGrams: \n"))

bmi = weight / (height**2)

if (bmi < 18.5):
    print("Your are Underweight.")
elif (bmi >= 18.5 and bmi<25):
    print("You are normal weight.")
else:
    print("You are overweight.")
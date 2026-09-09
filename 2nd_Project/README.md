# 🏋️ BMI Calculator

This is a simple Python program that calculates the **Body Mass Index (BMI)** based on the user's height and weight.

## What I Learned

In this project, I practiced:

* Taking user input using `input()`
* Converting input using `float()` and `int()`
* Performing mathematical calculations
* Using `if`, `elif`, and `else` statements
* Using comparison and logical operators
* Displaying results based on conditions

## How It Works

1. The program asks the user to enter their height in meters.
2. It asks the user to enter their weight in kilograms.
3. BMI is calculated using:

`BMI = weight / height²`

4. The program checks the BMI using conditional statements.

* BMI below `18.5` → Underweight
* BMI from `18.5` to below `25` → Normal weight
* BMI `25` or above → Overweight

## Code

```python
height = float(input("Enter your height in Meters: \n"))

weight = int(input("Enter your weight in KiloGrams: \n"))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("You are Underweight.")

elif bmi >= 18.5 and bmi < 25:
    print("You are normal weight.")

else:
    print("You are overweight.")
```

## Example

```text
Enter your height in Meters:
1.75

Enter your weight in KiloGrams:
70

You are normal weight.
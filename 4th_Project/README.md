# 🍕 Python Pizza Deliveries

This is a simple Python program that calculates the total bill for a pizza order based on the **pizza size, pepperoni, and extra cheese** selected by the user.

## What I Learned

In this project, I practiced:

* Taking user input using `input()`
* Using `if`, `elif`, and `else` statements
* Using nested `if` statements
* Using logical operators like `or`
* Updating variables using `+=`
* Using f-strings to display the final bill
* Building a simple billing system using Python

## Pizza Pricing

| Pizza Size | Price |
| ---------- | ----: |
| Small (S)  |   $15 |
| Medium (M) |   $20 |
| Large (L)  |   $25 |

### Additional Charges

| Extra                            | Price |
| -------------------------------- | ----: |
| Pepperoni for Small Pizza        |    $2 |
| Pepperoni for Medium/Large Pizza |    $3 |
| Extra Cheese                     |    $1 |

## How It Works

1. The program asks the user to select a pizza size: `S`, `M`, or `L`.
2. It asks whether the user wants pepperoni.
3. It asks whether the user wants extra cheese.
4. The base price is added depending on the pizza size.
5. Additional charges are added for pepperoni and extra cheese.
6. The program displays the final bill.

## Code

```python id="1g3t6n"
print("----------Welcome to Python Pizza Deliveries----------")

# Input to take the size of the pizza
size = input("What size do you want? S, M or L: ")

# Asking user if they need pepperoni
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")

# Asking user if they need extra cheese
extra_cheese = input("Do you want cheese on your pizza? Y or N: ")

total_bill = 0

if size == 'S' or size == 's':
    total_bill += 15

elif size == 'M' or size == 'm':
    total_bill += 20

elif size == 'L' or size == 'l':
    total_bill += 25

else:
    print("!!! Please select the appropriate size.")

if pepperoni == 'Y' or pepperoni == 'y':

    if size == 'S' or size == 's':
        total_bill += 2

    else:
        total_bill += 3

if extra_cheese == 'Y' or extra_cheese == 'y':
    total_bill += 1

# Output
print(f"Your Total bill is ${total_bill}.")
```

## Example Output

```text id="6b1fqd"
----------Welcome to Python Pizza Deliveries----------

What size do you want? S, M or L: M
Do you want pepperoni on your pizza? Y or N: Y
Do you want cheese on your pizza? Y or N: Y

Your Total bill is $24.
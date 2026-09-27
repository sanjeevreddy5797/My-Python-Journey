# ☕ Coffee Machine Program

A command-line **Coffee Machine simulator** built using Python as part of my **100 Days of Python** learning journey.

The program simulates a real coffee machine where users can:

- Order Espresso
- Order Latte
- Order Cappuccino
- Insert coins
- Receive change
- Check available resources
- Check machine profit
- Turn off the machine

## 🎯 Project Objective

The goal of this project is to simulate the basic operations of a coffee machine.

When a customer selects a drink, the program:

1. Checks whether enough ingredients are available.
2. Asks the customer to insert coins.
3. Calculates the total money inserted.
4. Checks whether the payment is sufficient.
5. Returns change when necessary.
6. Deducts the ingredients used.
7. Makes the coffee.
8. Adds the drink cost to the machine's profit.

## 🧠 Concepts I Practiced

Through this project, I practiced:

- Python dictionaries
- Nested dictionaries
- Functions
- Function parameters
- Return values
- `while` loops
- `for` loops
- Conditional statements
- Global variables
- User input
- Resource management
- Mathematical calculations
- Simulating transactions
- Breaking a larger program into smaller functions

---

# 📋 Coffee Menu

The available drinks are stored in a nested dictionary:

```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
```

Each drink contains two important pieces of information:

```text
Drink
 ├── Ingredients
 │    ├── Water
 │    ├── Milk
 │    └── Coffee
 │
 └── Cost
```

For example:

```python
MENU["latte"]
```

contains:

```python
{
    "ingredients": {
        "water": 200,
        "milk": 150,
        "coffee": 24
    },
    "cost": 2.5
}
```

---

# 🧃 Machine Resources

The coffee machine starts with:

```python
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
```

The units are:

```text
Water  → ml
Milk   → ml
Coffee → grams
```

The machine also starts with:

```python
profit = 0
```

As customers purchase drinks, the profit increases.

---

# 🔍 Checking Resources

Before accepting payment, the machine checks whether enough ingredients are available.

```python
def is_resource_sufficient(order_ingredients):

    for item in order_ingredients:

        if order_ingredients[item] > resources[item]:

            print(f"Sorry! there is not enough {item}.")

            return False

    return True
```

Suppose the customer orders a Latte.

A Latte requires:

```text
Water  = 200 ml
Milk   = 150 ml
Coffee = 24 g
```

If the machine contains:

```text
Water  = 300 ml
Milk   = 200 ml
Coffee = 100 g
```

all ingredients are available, so the function returns:

```python
True
```

But if only `100 ml` of water remains:

```text
Required = 200 ml
Available = 100 ml
```

the program displays:

```text
Sorry! there is not enough water.
```

and returns:

```python
False
```

---

# 🪙 Processing Coins

The customer can insert four types of coins:

| Coin | Value |
|---|---:|
| Quarter | $0.25 |
| Dime | $0.10 |
| Nickel | $0.05 |
| Penny | $0.01 |

The program calculates the total using:

```python
def process_coins():

    print("Please insert coins.")

    total = int(input("How many quarters?: ")) * 0.25

    total += int(input("How many dimes?: ")) * 0.10

    total += int(input("How many nickels?: ")) * 0.05

    total += int(input("How many pennies?: ")) * 0.01

    return total
```

For example:

```text
4 quarters = 4 × $0.25 = $1.00
5 dimes    = 5 × $0.10 = $0.50
```

Total:

```text
$1.00 + $0.50 = $1.50
```

---

# 💰 Checking the Transaction

The payment is checked using:

```python
def is_transaction_successful(money_received, drink_cost):
```

If:

```text
Money received >= Drink cost
```

the transaction succeeds.

For example:

```text
Latte price = $2.50
Money inserted = $3.00
```

Change:

```text
$3.00 - $2.50 = $0.50
```

The program displays:

```text
Here is $0.5 in change.
```

The drink price is then added to the machine's profit.

```python
global profit
profit += drink_cost
```

---

# ❌ Insufficient Payment

Suppose:

```text
Cappuccino price = $3.00
Money inserted = $2.00
```

Since:

```text
$2.00 < $3.00
```

the program displays:

```text
Sorry that's not enough money. Money refunded.
```

The coffee is not made and the resources are not deducted.

---

# ☕ Making the Coffee

Once the resources and payment have been validated, the coffee is made:

```python
def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕")
```

For example, suppose the machine has:

```text
Water  = 300 ml
Milk   = 200 ml
Coffee = 100 g
```

A Latte requires:

```text
Water  = 200 ml
Milk   = 150 ml
Coffee = 24 g
```

After making the Latte:

```text
Water  = 100 ml
Milk   = 50 ml
Coffee = 76 g
```

The program then displays:

```text
Here is your latte ☕
```

---

# 📊 Machine Report

Entering:

```text
report
```

shows the remaining resources and total money earned.

Example:

```text
Water: 100 ml
Milk: 50 ml
Coffee: 76 g
Money: $2.5
```

This information comes from:

```python
print(f"Water: {resources['water']} ml")
print(f"Milk: {resources['milk']} ml")
print(f"Coffee: {resources['coffee']} g")
print(f"Money: ${profit}")
```

---

# 📴 Turning Off the Machine

Entering:

```text
off
```

changes:

```python
is_on = False
```

which stops the main loop and turns off the coffee machine.

---

# 💻 Complete Code

```python
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


profit = 0


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when the order can be made,
    False if ingredients are insufficient."""

    for item in order_ingredients:

        if order_ingredients[item] > resources[item]:

            print(f"Sorry! There is not enough {item}.")

            return False

    return True


def process_coins():
    """Returns the total value of the coins inserted."""

    print("Please insert coins.")

    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when payment is accepted,
    or False when money is insufficient."""

    if money_received >= drink_cost:

        change = round(
            money_received - drink_cost,
            2
        )

        if change > 0:
            print(f"Here is ${change} in change.")

        global profit

        profit += drink_cost

        return True

    else:

        print(
            "Sorry that's not enough money. "
            "Money refunded."
        )

        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct required ingredients from resources."""

    for item in order_ingredients:

        resources[item] -= order_ingredients[item]

    print(f"Here is your {drink_name} ☕")


is_on = True


while is_on:

    choice = input(
        "What would you like? "
        "(espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":

        is_on = False

    elif choice == "report":

        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${profit}")

    else:

        drink = MENU[choice]

        if is_resource_sufficient(
            drink["ingredients"]
        ):

            payment = process_coins()

            if is_transaction_successful(
                payment,
                drink["cost"]
            ):

                make_coffee(
                    choice,
                    drink["ingredients"]
                )
```

---

# 🔄 Program Flow

```text
                 START
                   ↓
        What would you like?
                   ↓
     ┌─────────────┼─────────────┐
     ↓             ↓             ↓
   Drink         Report          Off
     ↓             ↓             ↓
Check Resources  Display       Turn Off
     ↓           Resources
Enough?
 /       \
NO        YES
↓          ↓
Reject   Insert Coins
           ↓
      Calculate Money
           ↓
      Enough Money?
        /       \
      NO         YES
      ↓           ↓
   Refund     Calculate Change
                  ↓
             Add to Profit
                  ↓
          Deduct Ingredients
                  ↓
             Make Coffee ☕
                  ↓
             Next Order
```

---

# 🖥️ Example Output

```text
What would you like? (espresso/latte/cappuccino): latte

Please insert coins.

How many quarters?: 10
How many dimes?: 2
How many nickels?: 0
How many pennies?: 0

Here is $0.2 in change.

Here is your latte ☕
```

Checking the report afterward:

```text
What would you like? (espresso/latte/cappuccino): report

Water: 100 ml
Milk: 50 ml
Coffee: 76 g
Money: $2.5
```

---

# 🔑 Important Concept — Nested Dictionaries

One of the most important concepts in this project is accessing information from nested dictionaries.

For example:

```python
drink = MENU["latte"]
```

gives:

```python
{
    "ingredients": {
        "water": 200,
        "milk": 150,
        "coffee": 24
    },
    "cost": 2.5
}
```

Then:

```python
drink["cost"]
```

returns:

```text
2.5
```

while:

```python
drink["ingredients"]
```

returns:

```python
{
    "water": 200,
    "milk": 150,
    "coffee": 24
}
```

This helped me understand how real-world information can be represented using nested Python dictionaries.

---

# 🚀 Future Improvements

I can improve this project by:

- Handling invalid drink names
- Validating coin input
- Adding a refill option
- Adding more drinks
- Allowing different drink sizes
- Improving money calculations
- Creating an OOP version of the coffee machine
- Building a graphical interface


Through this project, I learned how several smaller functions can work together:

```text
is_resource_sufficient()
          ↓
     process_coins()
          ↓
is_transaction_successful()
          ↓
      make_coffee()
```

The biggest lesson from this project was learning how to break a larger real-world problem into smaller functions, with each function having one clear responsibility.
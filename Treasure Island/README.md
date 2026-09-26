# 🏝️ Treasure Island

This is a simple **text-based adventure game** built using Python.

The player's mission is to find the hidden treasure by making the correct decisions at different stages of the game.

Each decision changes the path of the game. A wrong decision can result in **Game Over**, while the correct choices lead to the treasure. 🏆

## What I Learned

In this project, I practiced:

* Taking user input using `input()`
* Using `if`, `elif`, and `else` statements
* Using **nested conditional statements**
* Using `.lower()` to handle uppercase and lowercase input
* Creating and calling a function
* Understanding decision-based program flow
* Creating a simple text-based adventure game

## How the Game Works

The player starts at a crossroad and must make a series of decisions.

```text
START
  |
  |-- Left
  |     |
  |     |-- Wait
  |     |     |
  |     |     |-- Yellow → 🏆 You Win!
  |     |     |
  |     |     |-- Red → 🔥 Game Over
  |     |     |
  |     |     |-- Blue → 🐺 Game Over
  |     |
  |     |-- Swim → 🐊 Game Over
  |
  |-- Right → 🕳️ Game Over
```

The winning path is:

```text
Left → Wait → Yellow → Treasure 🏆
```

## Code

```python
def treasurepic():
    print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."   . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')


print("----------Welcome to Treasure Island----------")
print("----Your Mission is to find the treasure----")

direction = input(
    "You're at a crossroad, where do you want to go? "
    "Type ('left' or 'right'): "
).lower()

if direction == 'left':

    decision = input(
        "You've come to a lake. There is an island in the middle of the lake. "
        "Type 'wait' for the boat or 'swim' to swim across lake: "
    ).lower()

    if decision == 'wait':

        colour = input(
            "You've crossed the lake. Which door do you want to select "
            "'red', 'blue', 'yellow': "
        ).lower()

        if colour == 'yellow':
            print("Hooray!!! You won the Treasure...")
            treasurepic()

        else:
            if colour == 'red':
                print("It's a room full of fire. Game Over.")

            elif colour == 'blue':
                print("You enter into a room of beasts. Game Over.")

            else:
                print("Hooray! You won the treasure...")
                treasurepic()

    else:
        print("You were eaten by Crocodiles. Game Over.")

else:
    print("OOPS! You fell into a hole. Game Over.")
```

## Example Winning Output

```text
----------Welcome to Treasure Island----------
----Your Mission is to find the treasure----

You're at a crossroad, where do you want to go?
left

You've come to a lake.
wait

Which door do you want to select?
yellow

Hooray!!! You won the Treasure...
```

The treasure ASCII art is then displayed.

## Concepts Used

### Conditional Statements

The game uses:

```python
if
elif
else
```

to decide what should happen based on the player's choices.

### Nested Conditions

An `if` statement is placed inside another `if` statement to create multiple levels of decisions.

For example:

```python
if direction == "left":

    if decision == "wait":

        if colour == "yellow":
            print("You Win!")
```

### `.lower()`

The `.lower()` method converts the user's input to lowercase.

For example:

```python
direction = input("Left or Right? ").lower()
```

Therefore:

```text
LEFT → left
Left → left
left → left
```

This makes input handling easier.

### Function

The `treasurepic()` function stores the ASCII treasure image:

```python
def treasurepic():
    print("Treasure Image")
```

It is called when the player wins:

```python
treasurepic()
```
Through this project, I practiced Python conditional statements by building a small interactive game where the program's output changes based on the decisions made by the user.
# 🎯 Number Guessing Game

A command-line **Number Guessing Game** built using Python as part of my **100 Days of Python** learning journey.

The computer randomly chooses a number between **1 and 100**, and the player has to guess the number before running out of attempts.

The player can select between two difficulty levels:

* 🟢 Easy — 10 attempts
* 🔴 Hard — 5 attempts

---

## 🎮 How the Game Works

1. The computer randomly selects a number between `1` and `100`.
2. The player chooses a difficulty level.
3. The player enters a guess.
4. The program tells the player whether the guess is:

   * Too high
   * Too low
   * Correct
5. An attempt is removed after every incorrect guess.
6. The game continues until:

   * The player guesses correctly, or
   * The player runs out of attempts.

---

## 🧠 Concepts I Practiced

Through this project, I practiced:

* Python functions
* Function return values
* Constants
* `while` loops
* `if / elif / else`
* Random numbers
* `random.randint()`
* User input
* Type conversion using `int()`
* Comparison operators
* Managing game state
* Controlling the number of attempts
* Importing ASCII art from another module

---

## 📁 Project Structure

```text
Number-Guessing-Game/
│
├── main.py
└── art.py
```

The `art.py` file contains the ASCII-art logo:

```python
from art import logo
```

The logo is displayed using:

```python
print(logo)
```

---

## 🎲 Generating the Secret Number

The computer chooses a random number using:

```python
number = random.randint(1, 100)
```

`random.randint(1, 100)` generates a random integer from:

```text
1 → 100
```

including both `1` and `100`.

For example:

```text
Computer secretly chooses:

67
```

The player then tries to find `67`.

---

## ⚙️ Difficulty Levels

Two constants are created:

```python
EASY_TURNS = 10
HARD_TURNS = 5
```

The user chooses:

```text
easy
```

or:

```text
hard
```

The `no_of_lives()` function determines the number of attempts:

```python
def no_of_lives():

    if difficulty == 'easy':
        return EASY_TURNS

    elif difficulty == 'hard':
        return HARD_TURNS
```

Therefore:

```text
easy → 10 attempts
hard → 5 attempts
```

---

## 🔄 Game Loop

The game starts by getting the number of attempts:

```python
attempts = no_of_lives()
```

The game continues while attempts are available:

```python
while attempts != 0:
```

After every incorrect guess:

```python
attempts -= 1
```

For example:

```text
Starting attempts = 5

Wrong guess → 4
Wrong guess → 3
Wrong guess → 2
Wrong guess → 1
Wrong guess → 0
```

When the attempts reach `0`, the game ends.

---

## 📈 Too High

If:

```python
guessed_number > number
```

the program displays:

```text
Too high.
```

For example:

```text
Secret number = 50
Guess = 75

75 > 50

Too high.
```

---

## 📉 Too Low

If the guess is smaller than the secret number:

```python
else:
    print("Too low.")
```

For example:

```text
Secret number = 50
Guess = 30

30 < 50

Too low.
```

---

## 🎉 Correct Guess

The program checks:

```python
if guessed_number == number:
```

If the player finds the correct number:

```python
print(f"You got it! The answer was {guessed_number}.")
return
```

The `return` immediately exits the `game()` function.

For example:

```text
Secret number = 67
Guess = 67

You got it! The answer was 67.
```

---

## 💻 Complete Code

```python
import random
from art import logo

print(logo)

EASY_TURNS = 10
HARD_TURNS = 5

print("----------Welcome to the Number Guessing Game!----------")
print("I'm thinking of a number between 1 and 100")

number = random.randint(1, 100)

difficulty = input(
    "Choose a difficulty. Type 'easy' or 'hard': "
).lower()


def no_of_lives():

    if difficulty == 'easy':
        return EASY_TURNS

    elif difficulty == 'hard':
        return HARD_TURNS


def game():

    attempts = no_of_lives()

    while attempts != 0:

        print(
            f"You have {attempts} attempts remaining "
            "to guess the number."
        )

        guessed_number = int(input("Make a guess: "))

        if guessed_number == number:

            print(
                f"You got it! The answer was {guessed_number}."
            )

            return

        elif guessed_number > number:

            print("Too high.")

        else:

            print("Too low.")

        attempts -= 1

        if attempts > 1:
            print("Guess Again.")

    print("You've run out of guesses. Run the Game Again.")


game()
```

---

## 🔄 Program Flow

```text
START
  ↓
Display Logo
  ↓
Generate Random Number
Between 1 and 100
  ↓
Choose Difficulty
  ↓
┌─────────────────────┐
│ Easy → 10 Attempts  │
│ Hard → 5 Attempts   │
└─────────────────────┘
  ↓
Enter Guess
  ↓
Is Guess Correct?
 /             \
YES             NO
 ↓               ↓
YOU WIN      Compare Guess
                ↓
          ┌─────┴─────┐
          ↓           ↓
      Too High     Too Low
          \           /
           ↓         ↓
          attempts -= 1
                ↓
         Attempts Left?
           /       \
         YES        NO
          ↓          ↓
      Guess Again   Lose
```

---

## 🖥️ Example Output

```text
----------Welcome to the Number Guessing Game!----------

I'm thinking of a number between 1 and 100

Choose a difficulty.
Type 'easy' or 'hard': hard

You have 5 attempts remaining to guess the number.

Make a guess: 50
Too low.
Guess Again.

You have 4 attempts remaining to guess the number.

Make a guess: 75
Too high.
Guess Again.

You have 3 attempts remaining to guess the number.

Make a guess: 63
Too low.
Guess Again.

You have 2 attempts remaining to guess the number.

Make a guess: 67

You got it! The answer was 67.
```

---

## 🔑 Understanding `return`

One important concept used in this project is:

```python
return
```

When the player guesses correctly:

```python
if guessed_number == number:
    print(f"You got it! The answer was {guessed_number}.")
    return
```

`return` immediately stops the `game()` function.

Without it, the game loop could continue even after the player has guessed the correct answer.

---

## 🔑 Understanding `attempts -= 1`

This:

```python
attempts -= 1
```

is shorthand for:

```python
attempts = attempts - 1
```

If:

```text
attempts = 5
```

after one incorrect guess:

```text
attempts = 4
```

This is how the program keeps track of the player's remaining chances.

---

## 🚀 Future Improvements

I can improve this project in the future by:

* Handling invalid difficulty input
* Making `no_of_lives()` accept difficulty as a parameter
* Allowing the player to restart the game
* Checking whether guesses are between `1` and `100`
* Handling non-numeric input
* Showing the correct answer when the player loses
* Adding multiple difficulty levels
* Tracking the number of games won

---


Through this project, I practiced combining:

```text
Functions
   +
Random Numbers
   +
While Loops
   +
Conditionals
   +
Constants
   +
Game State
        ↓
Number Guessing Game 🎯
```

The main lesson from this project was learning how to use functions and loops together to control a game with a limited number of attempts.

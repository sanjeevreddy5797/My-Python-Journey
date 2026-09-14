# 🎯 Hangman Game

This is a simple **Hangman Game built using Python**.

The computer randomly selects a fruit name, and the player has to guess the word **one letter at a time**.

The player starts with **6 lives**. Every incorrect guess reduces one life and updates the Hangman picture. The game ends when the player either guesses the complete word or loses all lives.

## What I Learned

In this project, I practiced:

* Importing Python modules
* Creating and using custom modules
* Using `random.choice()`
* Working with lists
* Using `for` loops
* Using `while` loops
* Using `range()` and `len()`
* Accessing characters using indexes
* Updating list elements
* Using `if` conditions
* Using `in` and `not in`
* Using Boolean variables
* Tracking game state
* Building a complete interactive game

## Project Structure

The project is divided into three Python files:

```text
Hangman-Game/
│
├── main.py
├── HangManPics.py
└── FruitNames.py
```

### `main.py`

Contains the main game logic.

### `FruitNames.py`

Contains the list of fruit names from which the computer randomly chooses a word.

### `HangManPics.py`

Contains the different Hangman ASCII-art stages.

## How the Game Works

The player starts with:

```python
lives = 6
```

The computer randomly chooses a fruit:

```python
choosen_name = random.choice(FruitNames.fruits).lower()
```

For example:

```text
mango
```

The program creates a hidden representation:

```text
['_', '_', '_', '_', '_']
```

The player then guesses one letter at a time.

Suppose the player guesses:

```text
a
```

The display becomes:

```text
['_', 'a', '_', '_', '_']
```

If the player later guesses:

```text
g
```

it becomes:

```text
['_', 'a', '_', 'g', '_']
```

The game continues until the player wins or loses all 6 lives.

## Game Flow

```text
START
  ↓
Set lives = 6
  ↓
Choose random fruit
  ↓
Create _ _ _ _ representation
  ↓
Ask player for a letter
  ↓
Is letter in the word?
  │
  ├── YES → Reveal letter
  │
  └── NO → Reduce a life
  ↓
Check result
  │
  ├── No "_" remaining → YOU WIN 🏆
  │
  ├── Lives = 0 → GAME OVER 💀
  │
  └── Otherwise → Guess again
```

## Main Game Code

```python
import random

import HangManPics
import FruitNames

lives = 6

print("---------Welcome to HangMan Game----------")

choosen_name = random.choice(FruitNames.fruits).lower()

display = []

for i in range(len(choosen_name)):
    display.append('_')

print(display)

gameover = False

while not gameover:

    guessed_letter = input("Guess a letter: ").lower()

    for position in range(len(choosen_name)):

        letter = choosen_name[position]

        if letter == guessed_letter:
            display[position] = guessed_letter
            print(display)

    if guessed_letter not in choosen_name:

        lives -= 1

        if lives == 0:
            gameover = True
            print("You lose, Game Over.")

    if '_' not in display:
        gameover = True
        print("You won the game.")

    print(HangManPics.HANGMAN_PICS[lives])

    print(f"Only {lives} lives left.")

print(f"Your word is {choosen_name}.")
```

## Fruit Names Module

`FruitNames.py` contains:

```python
fruits = [
    "Apple", "Banana", "Orange", "Mango", "Grapes",
    "Pineapple", "Papaya", "Watermelon", "Strawberry", "Blueberry",
    "Kiwi", "Guava", "Pomegranate", "Peach", "Plum",
    "Cherry", "Litchi", "Pear", "Apricot", "Fig"
]
```

The program accesses this list using:

```python
FruitNames.fruits
```

and randomly chooses a fruit using:

```python
random.choice(FruitNames.fruits)
```

## Hangman Pictures Module

`HangManPics.py` contains the different stages of the Hangman drawing.

They are stored inside:

```python
HANGMAN_PICS = [
    # Hangman stages
]
```

The correct picture is displayed using:

```python
HangManPics.HANGMAN_PICS[lives]
```

As the number of lives decreases, the Hangman drawing progresses.

## Example Gameplay

```text
---------Welcome to HangMan Game----------

['_', '_', '_', '_', '_']

Guess a letter: a

['_', 'a', '_', '_', '_']

Only 6 lives left.

Guess a letter: x

Only 5 lives left.

Guess a letter: m

['m', 'a', '_', '_', '_']

Guess a letter: n

['m', 'a', 'n', '_', '_']

Guess a letter: g

['m', 'a', 'n', 'g', '_']

Guess a letter: o

['m', 'a', 'n', 'g', 'o']

You won the game.

Your word is mango.
```

## Important Concepts

### Random Word Selection

```python
choosen_name = random.choice(FruitNames.fruits).lower()
```

`random.choice()` randomly selects one fruit from the list.

### Creating the Hidden Word

```python
for i in range(len(choosen_name)):
    display.append('_')
```

If the word is:

```text
apple
```

the program initially creates:

```text
['_', '_', '_', '_', '_']
```

### Finding the Correct Position

The program checks every character:

```python
for position in range(len(choosen_name)):
    letter = choosen_name[position]

    if letter == guessed_letter:
        display[position] = guessed_letter
```

This allows the program to reveal the guessed letter at its correct position.

### Tracking Lives

For an incorrect guess:

```python
if guessed_letter not in choosen_name:
    lives -= 1
```

The player starts with:

```text
6 lives
```

and loses one life after each wrong guess.

### Checking for a Win

```python
if '_' not in display:
```

When there are no `_` characters remaining, every letter has been discovered and the player wins.

## Future Improvements 🚀

As I learn more Python, I can improve this game by:

* Preventing the same incorrect guess from reducing lives multiple times
* Keeping track of previously guessed letters
* Validating that the user enters only one letter
* Displaying the hidden word more neatly
* Adding difficulty levels
* Adding more word categories
* Allowing the player to restart the game
* Organizing the game using functions


Through this project, I combined many concepts I learned earlier—including lists, loops, conditional statements, randomization, modules, indexing, and Boolean values—to build a complete interactive Hangman game.
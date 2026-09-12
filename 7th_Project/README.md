# ✊📄✂️ Rock Paper Scissors Game

This is a simple Python implementation of the classic **Rock Paper Scissors** game.

The player selects Rock, Paper, or Scissors, and the computer randomly chooses its move. The program then compares both choices and determines the winner.

## What I Learned

In this project, I practiced:

* Importing Python modules
* Creating custom modules
* Using the `random` module
* Working with lists
* Using conditional statements (`if`, `elif`, `else`)
* Generating random numbers
* Displaying ASCII art
* Building a simple game using Python

## Game Rules

```text
Rock beats Scissors
Scissors beats Paper
Paper beats Rock
```

### Input Mapping

```text
0 → Rock
1 → Paper
2 → Scissors
```

## How the Program Works

### Step 1

The user selects:

```python
user_choice = int(input(
    "Enter the number '0 for rock', '1 for paper' and '2 for scissors': "
))
```

### Step 2

The computer randomly chooses a move:

```python
computer_choice = random.randint(0, 2)
```

Possible values:

```text
0 → Rock
1 → Paper
2 → Scissors
```

### Step 3

The program compares both choices and decides:

* Draw
* User Wins
* Computer Wins

### Step 4

ASCII art is displayed for both the user and computer choices.

## Project Structure

```text
Rock-Paper-Scissors/
│
├── main.py
└── RPS_Module.py
```

### RPS_Module.py

This module stores the ASCII art representations of:

* Rock
* Paper
* Scissors

and keeps them inside a list:

```python
list1 = [rock, paper, scissors]
```

This allows easy access using indexes:

```python
RPS_Module.list1[0]
```

returns Rock.

## Example Output

```text
Enter the number
0 for rock
1 for paper
2 for scissors

0

Computer choice:

Paper

Your choice:

Rock

You lost!!!
```

## Concepts Used

### Random Number Generation

```python
random.randint(0, 2)
```

Generates a random number between 0 and 2.

Example:

```text
0
1
2
```

Each number represents Rock, Paper, or Scissors.

### Lists

The ASCII art is stored in a list:

```python
list1 = [rock, paper, scissors]
```

Example:

```python
list1[0]
```

returns Rock.

### Conditional Statements

The winner is determined using:

```python
if
elif
else
```

For example:

```python
if user_choice == computer_choice:
    print("It's a draw!")
```

## Improvements for Future Versions

Some improvements that can be added later:

* Fix invalid input checking
* Allow multiple rounds
* Keep track of scores
* Add a replay option
* Use functions to reduce repeated code
* Handle non-numeric input using `try-except`

## Bugs Found During Development

### Invalid Input Condition

Current code:

```python
if(user_choice>=3 and user_choice<0):
```

This condition can never be true because a number cannot be both:

```text
Greater than or equal to 3
AND
Less than 0
```

Correct version:

```python
if(user_choice >= 3 or user_choice < 0):
```

or

```python
if user_choice not in [0, 1, 2]:
```

### Typo in Output

Current code:

```python
print(f"! ! !omputer choice :")
```

Should be:

```python
print(f"Computer choice :")